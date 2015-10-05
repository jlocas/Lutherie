using UnityEngine;
using System.Collections;

public class SpringGrid : MonoBehaviour {

	public GameObject blockPrefab;
	public GameObject anchorPrefab;

	[Space(20)] //block and grid settings
	public int sideLength;
	public float anchorHeight = -10f;
	public bool freezeEdges;
	public bool blocksCollision;

	[Space(20)] //spring settings
	public Vector3 spring;
	public Vector3 damper;
	public bool springCollision;

	[Space(20)]
	public bool repositionBlocks;
	public float reposSpeed;
	public float minDistance;
	public float minVelocity;

	private SpringGridBlock[,] blocks;

	private Vector3 oldAnchorPos;
	private float oldAnchorHeight = -10f;
	private bool oldFreezeEdges;
	private bool oldBlocksCollision;
	
	[Space(20)] //spring settings
	private Vector3 oldSpring;
	private Vector3 oldDamper;
	private bool oldSpringCollision;


	// Use this for initialization
	void Start () {
		InitOlds();
		CreateGrid();

		InvokeRepeating("PingBlocks", 0f, 1f);
	
	}
	
	// Update is called once per frame
	void Update () {
		UpdateParameters();
		Reposition();
	
	}

	/*
	 * *************************************************
	 * *************************************************
	 * *************************************************
	 * ALL THE FUNCTIONS FOR INITIALIZATION OF THE GRID
	 * *************************************************
	 * *************************************************
	 * *************************************************
	 */
	private void CreateGrid()
	{
		blocks = new SpringGridBlock[sideLength, sideLength];

		CreateBlocks();
		SetupSprings();
		SetFreezeEdges(freezeEdges);
	}

	private void CreateBlocks()
	{
		GameObject blockContainer = new GameObject();
		blockContainer.transform.SetParent(gameObject.transform);
		blockContainer.name = "Blocks";

		GameObject anchorContainer = new GameObject();
		anchorContainer.transform.SetParent(gameObject.transform);
		anchorContainer.name = "Anchors";

		for(int x = 0; x < sideLength; x++){
			for(int z = 0; z < sideLength; z++){
				//creation of blocks
				blocks[x,z] = new SpringGridBlock();

				GameObject newBlock = Instantiate(blockPrefab, new Vector3(x, 0f, z), Quaternion.identity) as GameObject;
				newBlock.transform.SetParent(blockContainer.transform);
				newBlock.name = string.Format("{0}, {1}",x, z);
				newBlock.GetComponent<BoxCollider>().enabled = blocksCollision;
				blocks[x,z].Block = newBlock;

				//creation of anchors
				GameObject newAnchor = Instantiate(anchorPrefab, new Vector3(x, 0f, z), Quaternion.identity) as GameObject;
				newAnchor.transform.SetParent(anchorContainer.transform);
				newAnchor.name = string.Format("{0}, {1}",x, z);
				newAnchor.transform.Rotate(new Vector3(90f, 0f, 0f));
				blocks[x,z].Anchor = newAnchor;

				//fill the component arrays
				blocks[x,z].Body = blocks[x,z].Block.GetComponent<Rigidbody>();
				blocks[x,z].Collider = blocks[x,z].Block.GetComponent<BoxCollider>();
				blocks[x,z].Springs = new SpringJoint[3];
				blocks[x,z].IsRepositioning = false;
				for(int i = 0; i < 3; i++)
				{
					blocks[x,z].Springs[i] = blocks[x,z].Block.AddComponent<SpringJoint>();
				}
			}
		}
		anchorContainer.transform.position = new Vector3(0f, anchorHeight, 0f);
	}

	private void SetupSprings()
	{
		for(int x = 0; x < sideLength; x++){
			for(int z = 0; z < sideLength; z++){

				if(x < sideLength-1)
				{
					blocks[x,z].Springs[0].connectedBody = blocks[x+1,z].Body;
					blocks[x,z].Springs[0].anchor = new Vector3(blocks[x,z].Block.transform.localScale.x * 0.5f, 0f, 0f);

					blocks[x,z].Springs[0].spring = spring.x;
					blocks[x,z].Springs[0].damper = damper.x;
					blocks[x,z].Springs[0].enableCollision = springCollision;
				}
				
				if(z < sideLength-1)
				{
					blocks[x,z].Springs[1].connectedBody = blocks[x,z+1].Body;
					blocks[x,z].Springs[1].anchor = new Vector3(0f, 0f, blocks[x,z].Block.transform.localScale.z * 0.5f);

					blocks[x,z].Springs[1].spring = spring.z;
					blocks[x,z].Springs[1].damper = damper.z;
					blocks[x,z].Springs[1].enableCollision = springCollision;
				}

				blocks[x,z].Springs[2].connectedBody = blocks[x,z].Anchor.GetComponent<Rigidbody>();
				blocks[x,z].Springs[2].anchor = new Vector3(0f, blocks[x,z].Block.transform.localScale.y * -0.5f, 0f);

				blocks[x,z].Springs[2].spring = spring.y;
				blocks[x,z].Springs[2].damper = damper.y;
				blocks[x,z].Springs[2].enableCollision = springCollision;

				foreach(SpringJoint joint in blocks[x,z].Springs)
				{
					if(joint.connectedBody == null)
					{
						Destroy(joint);
					}
				}
			}
		}
	}

	/*
	 * *************************************************
	 * *************************************************
	 * *************************************************
	 * ALL THE FUNCTIONS THAT ARE EXECUTED IN UPDATE
	 * *************************************************
	 * *************************************************
	 * *************************************************
	 */

	private void PingBlocks()
	{
		if(repositionBlocks){
			for(int x = 0; x < sideLength; x++){
				for(int z = 0; z < sideLength; z++){
					Vector3 targetPos = new Vector3(blocks[x,z].Anchor.transform.position.x, blocks[x,z].Anchor.transform.position.y + anchorHeight * -1, blocks[x,z].Anchor.transform.position.z);
					if(blocks[x,z].Block.transform.position != targetPos){
						blocks[x,z].IsRepositioning = true;
					}
				}
			}
		}

	}

	void Reposition() //reposition blocks[x,z]
	{
		for(int x = 0; x < sideLength; x++)	{
			for(int z = 0; z <sideLength; z++){

				if(blocks[x,z].IsRepositioning)
				{
					SpringGridBlock block = blocks[x,z];
					Vector3 currentPos = block.Block.transform.position;
					Vector3 targetPos = new Vector3(blocks[x,z].Anchor.transform.position.x, blocks[x,z].Anchor.transform.position.y + anchorHeight * -1, blocks[x,z].Anchor.transform.position.z);
					float velocity = block.Body.velocity.magnitude;
					float distance = Vector3.Distance(currentPos, targetPos);

					if(distance > minDistance && velocity < minVelocity)	{
						block.Block.transform.position = Vector3.Lerp(currentPos, targetPos, reposSpeed * Time.deltaTime);
					} else if (currentPos != targetPos && distance <= minDistance && velocity < minVelocity){
						block.Body.velocity = Vector3.zero;
						block.Body.angularVelocity = Vector3.zero;
						block.Block.transform.position = targetPos;
						block.IsRepositioning = false;
					}
				}

			}
		}
	}
	

	/*
	 * *************************************************************
	 * *************************************************************
	 * FUNCTIONS BELOW ARE GET, SET FUNCTIONS AND PARAMETER CHANGE CHECKS
	 * *************************************************************
	 * *************************************************************
	 */

	public SpringGridBlock GetBlock(int x, int z)
	{
		SpringGridBlock block = blocks[x,z];
		return block;
	}


	public int GetSideLength()
	{
		return sideLength;
	}

	private float GetHighestVelocity()
	{
		float maxVel = 0f;
		
		for(int x = 0; x < sideLength; x++){
			for(int z = 0; z < sideLength; z++){
				float velocity = blocks[x,z].Body.velocity.magnitude;
				
				if(velocity > maxVel){
					maxVel = velocity;
				}
			}
		}

		return maxVel;
	}

	private void SetFreezeEdges(bool tog)
	{
		RigidbodyConstraints constraints = RigidbodyConstraints.FreezeRotation;

		if(tog)
		{
			constraints = RigidbodyConstraints.FreezeAll;
		}

		for(int i = 0; i < sideLength; i++)
		{
			blocks[0, i].Body.constraints = constraints;
			blocks[sideLength - 1, i].Body.constraints = constraints;
			blocks[i, 0].Body.constraints = constraints;
			blocks[i, sideLength - 1].Body.constraints = constraints;
		}
		
	}

	private void SetAnchorHeight(float newHeight)
	{
		for(int x = 0; x < sideLength; x++){
			for(int z = 0; z < sideLength; z++){
				Vector3 pos = blocks[x,z].Anchor.transform.position;
				pos = new Vector3(pos.x, newHeight, pos.z);
				blocks[x,z].Anchor.transform.position = pos;
			}
		}
	}

	private void SetBlockCollision(bool tog)
	{
		for(int x = 0; x < sideLength; x++){
			for(int z = 0; z < sideLength; z++){
				blocks[x,z].Collider.enabled = tog;
			}
		}
	}

	private void SetSpring(Vector3 spr)
	{
		for(int x = 0; x < sideLength; x++){
			for(int z = 0; z < sideLength; z++){
				blocks[x,z].Springs[0].spring = spr.x;
				blocks[x,z].Springs[1].spring = spr.z;
				blocks[x,z].Springs[2].spring = spr.y;
			}
		}
	}

	private void SetDamper(Vector3 damp)
	{
		for(int x = 0; x < sideLength; x++){
			for(int z = 0; z < sideLength; z++){
				blocks[x,z].Springs[0].damper = damp.x;
				blocks[x,z].Springs[1].damper = damp.z;
				blocks[x,z].Springs[2].damper = damp.y;
			}
		}
	}

	private void SetSpringCollision(bool tog)
	{
		for(int x = 0; x < sideLength; x++){
			for(int z = 0; z < sideLength; z++){

				for(int i = 0; i < 3; i++)
				{
					blocks[x,z].Springs[i].enableCollision = tog;
				}
			}
		}
	}


	private void InitOlds()
	{
		oldAnchorHeight = anchorHeight;
		oldFreezeEdges = freezeEdges;
		oldBlocksCollision = blocksCollision;
		
		oldSpring = spring;
		oldDamper = damper;
		oldSpringCollision = springCollision;
	}

	private void UpdateParameters()
	{
		if(anchorHeight != oldAnchorHeight)
		{
			SetAnchorHeight(anchorHeight);
			oldAnchorHeight = anchorHeight;
		}

		if(freezeEdges != oldFreezeEdges)
		{
			SetFreezeEdges(freezeEdges);
			oldFreezeEdges = freezeEdges;
		}

		if(blocksCollision != oldBlocksCollision)
		{
			SetBlockCollision(blocksCollision);
			oldBlocksCollision = blocksCollision;
		}

		if(spring.magnitude != oldSpring.magnitude)
		{
			SetSpring(spring);
			oldSpring = spring;
		}

		if(damper.magnitude != oldDamper.magnitude)
		{
			SetDamper(damper);
			oldDamper = damper;
		}

		if(springCollision != oldSpringCollision)
		{
			SetSpringCollision(springCollision);
			oldSpringCollision = springCollision;
		}
	}
}
