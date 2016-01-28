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
	public bool spawnBalls;
	private int oldClockVal;
	

	
	public Vector2 size;
	private Vector2 realSize;

	public float SizeX {
		get {
			return realSize.x;
		}
		set {
			bounds.SizeX = value;
		}
	}
	
	public float SizeZ {
		get {
			return realSize.y;
		}
		set {
			bounds.SizeZ = value;
		}
	}

	public Vector2 center;
	private Vector2 realCenter;
	
	public float CenterX{
		get{
			return realCenter.x;
		}
		set{	
			bounds.CenterX = value;
		}
	}
	
	public float CenterZ{
		get{
			return realCenter.y;
		}
		set{
			bounds.CenterZ = value;
		}
	}

	void SpawnBall(){
		if(spawnBalls){
			GameObject newBall = Instantiate(ballPrefab, bounds.GetBallPosition(), Quaternion.identity) as GameObject;
			newBall.transform.parent = ballContainer.transform;
		}
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
	}

	void Update(){
		Tick ();
	}
}