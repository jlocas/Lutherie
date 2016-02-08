using UnityEngine;
using System.Collections;

public class Rain : MonoBehaviour {

	public GameObject ballPrefab;
	public GameObject ballContainer;
	public SpringGrid grid;
	public GameObject ballBoundsPrefab;
	public Clock clock;
	GameObject boundsGo;
	RainBounds bounds;
	[Space(20)]
	private int oldClockVal;
	

	
	public Vector3 size;
	public float SizeX {
		get {
			return size.x;
		}
		set {
			bounds.SizeX = value;
		}
	}
	
	public float SizeZ {
		get {
			return size.z;
		}
		set {
			bounds.SizeZ = value;
		}
	}

	public Vector3 center;
	public float CenterX{
		get{
			return center.x;
		}
		set{	
			bounds.CenterX = value;
		}
	}
	
	public float CenterZ{
		get{
			return center.z;
		}
		set{
			bounds.CenterZ = value;
		}
	}

	public float ballForce;
	public float BallForce{
		get{
			return ballForce;
		}
		set{
			ballForce = value;
		}
	}

	public bool spawnBalls;
	public float SpawnBalls{
		set{
			if(value > 0){
				spawnBalls = true;
			}
		}
	}
	
	void SpawnBall(){
		if(spawnBalls){
			GameObject newBall = Instantiate(ballPrefab, bounds.GetBallPosition(), Quaternion.identity) as GameObject;
			newBall.transform.parent = ballContainer.transform;
			newBall.GetComponent<Ball>().Force = BallForce;		}
	}

	void Tick(){
		if(clock.doubles != oldClockVal){
			SpawnBall();
			oldClockVal = clock.doubles;
		}
	}

	void Awake(){
		boundsGo = Instantiate(ballBoundsPrefab, new Vector3(0, 0.5f, 0), Quaternion.identity) as GameObject;
		bounds = boundsGo.GetComponent<RainBounds>();
		bounds.RangeCenter = grid.GetSideLength() * 0.5f - 1;
		bounds.gridSize = (float)grid.GetSideLength();

		bounds.CenterX = center.x;
		bounds.CenterZ = center.z;
		bounds.SizeX = size.x;
		bounds.SizeZ = size.z;
	}

	void Update(){
		Tick ();
	}
}