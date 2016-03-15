using UnityEngine;
using System.Collections;

public class Rain_2 : MonoBehaviour {

	public GameObject ballPrefab;
	public GameObject ballContainer;
	public GameObject ballParticleContainer;
	public SpringGrid grid;
	public GameObject ballBoundsPrefab;
	public OSCSender oscSend;
	public Clock clock;
	GameObject boundsGo;
	RainBounds bounds;
	[Space(20)]
	private int oldClockVal;
	private bool ballGate = true;

	
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
			} else if(value==0){
				spawnBalls = false;
			}
		}
	}

	public int spawnRate;
	public float SpawnRate{
		set{
			int val = (int)value;
			switch(val){
			case 1:
				spawnRate = 1;
				break;
			case 2:
				spawnRate = 2;
				break;
			case 3:
				spawnRate = 4;
				break;
			case 4:
				spawnRate = 8;
				break;
			case 5:
				spawnRate = 16;
				break;
			case 6:
				spawnRate = 32;
				break;
			case 7:
				spawnRate = 64;
				break;
			case 8:
				spawnRate = 128;
				break;
			}
		}
	}

	public void Spawn1Ball(float force){

		if(ballGate){
			GameObject newBall = Instantiate(ballPrefab, bounds.GetBallPosition(), Quaternion.identity) as GameObject;
			Ball_2 script = newBall.GetComponent<Ball_2>();
			newBall.transform.parent = ballContainer.transform;
			script.particleContainer = ballParticleContainer;
			script.Force = BallForce;		
			script.sender = oscSend;
			ballGate = false;
		}
		if(force == 0){
			ballGate = true;
		}

	}
	
	void SpawnBall(){
		if(spawnBalls){
			GameObject newBall = Instantiate(ballPrefab, bounds.GetBallPosition(), Quaternion.identity) as GameObject;
			Ball_2 script = newBall.GetComponent<Ball_2>();
			newBall.transform.parent = ballContainer.transform;
			script.particleContainer = ballParticleContainer;
			script.Force = BallForce;		
			script.sender = oscSend;
		}
	}

	void Tick(){


		if(clock.ticks - oldClockVal >= spawnRate){
			SpawnBall();
			oldClockVal = clock.ticks;
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