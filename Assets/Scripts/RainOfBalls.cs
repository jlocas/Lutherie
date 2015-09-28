using UnityEngine;
using System.Collections;

public class RainOfBalls : MonoBehaviour {

	public GameObject ballPrefab;
	public SpringGrid springGrid;
	public GameObject ballContainer;

	[Space(20)]
	public float bpm;
	public float tempoGridSize;
	public float ticks;

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


	// Use this for initialization
	void Start () {
		ticks = 60000 / bpm * tempoGridSize;

		gridLength = springGrid.GetSideLength();
		InvokeRepeating("Tick", ticks * 0.001f, ticks * 0.001f);
	
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
		//newBall.transform.SetParent(ballContainer.transform);
	}

	private void UpdatePosition()
	{
		realPosX = posX * gridLength;
		realPosZ = posZ * gridLength;

		gameObject.transform.position = new Vector3(realPosX, posY, realPosZ);
	}
}
