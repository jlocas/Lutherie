using UnityEngine;
using System.Collections;

public class RainOfBalls : MonoBehaviour {

	public GameObject ballPrefab;
	public SpringGrid springGrid;
	public GameObject ballContainer;
	public Clock clock;

	[Space(20)]
	public int sizeX;
	public int sizeZ;

	[Range(0,1)]
	public float posX;
	[Range(0,1)]
	public float posZ;
	private float realPosX;
	private float realPosZ;
	public float posY;
	private int gridLength;

	private Vector2 minBounds;
	private Vector2 maxBounds;

	public Pattern ballSize;


	// Use this for initialization
	void Start () {
		ballSize.Generate();

		gridLength = springGrid.GetSideLength();	
		InvokeRepeating("Tick", 0, clock.barDur*0.00025f);
	}
	
	// Update is called once per frame
	void Update () {
		UpdatePosition();
	
	}

	private void Tick()
	{
		CreateBall();
	}

	private void CreateBall()
	{
		Vector3 pos = new Vector3(realPosX + Random.Range(sizeX * -0.5f, sizeX * 0.5f), posY, realPosZ + Random.Range(sizeZ * -0.5f, sizeZ * 0.5f));
		GameObject newBall = Instantiate(ballPrefab, pos, Quaternion.identity) as GameObject;
		newBall.transform.SetParent(ballContainer.transform);

		float force = ballSize.ReadNext();
		newBall.GetComponent<Ball>().Force = force;
		float scale = 1f * force * 0.01f;
		newBall.transform.localScale = new Vector3(scale, scale, scale);
	}

	private void UpdatePosition()
	{
		realPosX = posX * gridLength;
		realPosZ = posZ * gridLength;

		gameObject.transform.position = new Vector3(realPosX, posY, realPosZ);
	}
}
