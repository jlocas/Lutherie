using UnityEngine;
using System.Collections;

public class Rain : MonoBehaviour {

	public GameObject ballPrefab;
	public GameObject ballContainer;
	public SpringGrid springGrid;
	public Clock clock;

	public NoteValues noteValues;

	[Space(20)]
	public Vector2 center;
	private Vector2 oldCenter = new Vector2();

	public Vector2 size;
	private Vector2 oldSize = new Vector2();

	public float height;

	private Vector2 minBounds;
	private Vector2 maxBounds;

	[Space(20)]
	public Pattern xPositionPattern;
	public Pattern zPositionPattern;

	public Pattern ballSize;
	public Pattern ballSpawn;

	private Pattern[] patterns;

	private int oldClockVal;


	// Use this for initialization
	void Start () {
		patterns = new Pattern[]{xPositionPattern, zPositionPattern, ballSize, ballSpawn};

		foreach(Pattern pat in patterns){
			pat.Generate();
		}
	
	}
	
	// Update is called once per frame
	private void Update () {
		UpdateBounds();
		Tick ();
	
	}

	private void UpdateBounds(){
		if(!Vector2.Equals(size, oldSize) || !Vector2.Equals(center, oldCenter)){

			minBounds.x = Mathf.Min(springGrid.sideLength, center.x - size.x);
			minBounds.y = Mathf.Min(springGrid.sideLength, center.y - size.y);

			maxBounds.x = Mathf.Max(springGrid.sideLength, center.x + size.x);
			maxBounds.y = Mathf.Max(springGrid.sideLength, center.y + size.y);

			oldSize = size;
			oldCenter = center;
		}
	}

	private void Tick(){

		if(clock.doubles != oldClockVal){
			if(ballSpawn.ReadNext() >= 0.5f){
				CreateBall();
			}
			oldClockVal = clock.doubles;
		}
	}

	private void CreateBall(){
		Vector3 pos = new Vector3( Mathf.Clamp( xPositionPattern.ReadNext() * size.x + center.x, minBounds.x, maxBounds.x ), 
		                          height, 
		                          Mathf.Clamp( zPositionPattern.ReadNext() * size.y + center.y, minBounds.y, maxBounds.y ));

		GameObject newBall = Instantiate(ballPrefab, pos, Quaternion.identity) as GameObject;
		newBall.transform.SetParent(ballContainer.transform);

		float force = ballSize.ReadNext();
		float scale = force * 0.005f;

		newBall.GetComponent<Ball>().Force = force;
		newBall.transform.localScale = new Vector3(scale, scale, scale);


	}

}
