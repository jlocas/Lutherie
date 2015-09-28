using UnityEngine;
using System.Collections;

public class SpringMesh1 : MonoBehaviour {

	public GameObject gridBlockObject;
	public GameObject gridBaseObject;

	[Space(20)]
	public int gridLength;
	public int gridSize;
	public float spring;
	public float damper;
	public float minDistance;
	public float maxDistance;
	public bool freezeEdges = false;

	private GameObject gridBase;
	private GameObject[,] gridBlocks;

	// Use this for initialization
	void Start () {
		InitGrid();
		CreateBase();
		CreateBlocks();
		AttachBlocks();

		if(freezeEdges)	{	FreezeEdges();	}
		InvokeRepeating("PingBlocks", 1f, 1f);	

	}

	void InitGrid()
	{
		gridSize = gridLength * gridLength;
		gridBlocks = new GameObject[gridLength, gridLength];

	}
	
	// Update is called once per frame
	void Update () {

	}

	void CreateBlocks()
	{
		for(int x = 0; x < gridLength; x++)
		{
			for(int z = 0; z < gridLength; z++)
			{
				GameObject newObj = Instantiate(gridBlockObject, new Vector3(x, 0f, z), Quaternion.identity) as GameObject;
				newObj.transform.SetParent(gameObject.transform);
				newObj.name = string.Format("{0}, {1}",x, z);
				gridBlocks[x,z] = newObj;
			}
		}
	}

	void CreateBase()
	{
		GameObject newObj = Instantiate(gridBaseObject, new Vector3(gridLength * 0.5f - 0.5f, -50f, gridLength * 0.5f - 0.5f), Quaternion.identity) as GameObject;

		newObj.transform.localScale = new Vector3(gridLength, gridLength, gridLength);
		newObj.transform.Rotate(new Vector3(90f, 0f, 0f));
		newObj.transform.SetParent(gameObject.transform);
		newObj.name = string.Format("Grid Base");
		gridBase = newObj;
	}
	
	void AttachBlocks()
	{
		for(int x = 0; x < gridLength; x++)
		{
			for(int z = 0; z < gridLength; z++)
			{

				SpringJoint[] springs = new SpringJoint[3]{
					gridBlocks[x,z].AddComponent<SpringJoint>(),
					gridBlocks[x,z].AddComponent<SpringJoint>(),
					gridBlocks[x,z].AddComponent<SpringJoint>()
				};

				if(x < gridLength-1)
				{
					springs[0].connectedBody = gridBlocks[x+1,z].GetComponent<Rigidbody>();
					springs[0].anchor = new Vector3(gridBlocks[x,z].transform.localScale.x * 0.5f, 0f, 0f);
				}

				if(z < gridLength-1)
				{
					springs[1].connectedBody = gridBlocks[x,z+1].GetComponent<Rigidbody>();
					springs[1].anchor = new Vector3(0f, 0f, gridBlocks[x,z].transform.localScale.z * 0.5f);
				}

				springs[2].connectedBody = gridBase.GetComponent<Rigidbody>();
				springs[2].anchor = new Vector3(0f, gridBlocks[x,z].transform.localScale.y * -0.5f, 0f);

				foreach(SpringJoint joint in springs)
				{
					joint.enableCollision = false;
					joint.spring = spring;
					joint.damper = damper;
					joint.enablePreprocessing = true;
					joint.minDistance = minDistance;
					joint.maxDistance = maxDistance;
				}

			}
		}
	}

	void FreezeEdges()
	{
		RigidbodyConstraints constraints = RigidbodyConstraints.FreezeAll;

		for(int i = 0; i < gridLength; i++)
		{
			gridBlocks[0, i].GetComponent<Rigidbody>().constraints = constraints;
			gridBlocks[gridLength - 1, i].GetComponent<Rigidbody>().constraints = constraints;
			gridBlocks[i, 0].GetComponent<Rigidbody>().constraints = constraints;
			gridBlocks[i, gridLength - 1].GetComponent<Rigidbody>().constraints = constraints;
		}

	}

	void PingBlocks()
	{
		float maxVel = 0f;

		for(int x = 0; x < gridLength; x++)
		{
			for(int z = 0; z < gridLength; z++)
			{
				float velocity = gridBlocks[x,z].GetComponent<Rigidbody>().velocity.magnitude;

				if(velocity > maxVel){
					maxVel = velocity;
				}
			}
		}

		if(maxVel < 0.1f)
		{
			for(int x = 0; x < gridLength; x++)	{
				for(int z = 0; z < gridLength; z++)	
				{
					//gridBlocks[x,z].GetComponent<SpringMeshBlock>().SetRepositionStatus(true);
				
				}
			}
		}
	}
}
