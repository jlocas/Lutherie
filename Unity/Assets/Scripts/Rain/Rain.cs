using UnityEngine;
using System.Collections;

public class Rain : MonoBehaviour {

	public GameObject ballPrefab;
	public GameObject ballContainer;
	public SpringGrid springGrid;
	public GameObject ballBoxPrefab;

	GameObject ballBox;
	[Space(20)]
	public Vector2 center;
	private Vector2 realCenter;

	public float CenterX{
		get{
			return realCenter.x;
		}
		set{
			center.x = Mathf.Clamp01(value);
			realCenter.x = center.x * (springGrid.GetSideLength() - 1);
			moveBallBox = true;
			CalculateBounds();
		}
	}

	public float CenterY{
		get{
			return realCenter.y;
		}
		set{
			center.y = Mathf.Clamp01(value);
			realCenter.y = center.y * (springGrid.GetSideLength() - 1);
			moveBallBox = true;
			CalculateBounds();
		}
	}

	public Vector2 size;
	private Vector2 realSize;
	public Vector2 minBounds;
	public Vector2 maxBounds;

	public float SizeX{
		get{
			return realSize.x;
		}
		set{
			size.x = Mathf.Clamp01(value);
			realSize.x = size.x * (springGrid.GetSideLength() - 1) + 1;
			scaleBallBox = true;
			CalculateBounds();
		}
	}

	public float SizeY{
		get{
			return realSize.y;
		}
		set{
			size.y = Mathf.Clamp01(value);
			realSize.y = size.y * (springGrid.GetSideLength() - 1) + 1;
			scaleBallBox = true;
			CalculateBounds();
		}
	}

	public float spawnHeight = 50f;
	private bool moveBallBox = false;
	private bool scaleBallBox = false;


	// Use this for initialization
	void Start () {
		ballBox = Instantiate(ballBoxPrefab, new Vector3(realCenter.x, 2f, realCenter.y), Quaternion.identity) as GameObject;
		ballBox.transform.Rotate(new Vector3(-90f, 0, 0));
	
	}
	
	// Update is called once per frame
	void Update () {
		UpdateBallBoxPos();
		UpdateBallBoxScale();
	}

	void UpdateBallBoxPos(){

		if(moveBallBox){
			Vector3 targetPos = new Vector3(realCenter.x, 2f, realCenter.y);

			if(Vector3.Distance(ballBox.transform.position, targetPos) <= 0.05f){
				ballBox.transform.position = targetPos;
				moveBallBox = false;
			} else if(ballBox.transform.position != targetPos){
				ballBox.transform.position = Vector3.Lerp(ballBox.transform.position, targetPos, Time.deltaTime*2f);
			} 
		}
	}

	void UpdateBallBoxScale(){
		if(scaleBallBox){
			Vector3 targetScale = new Vector3(maxBounds.x - minBounds.x + 1f, maxBounds.y - minBounds.y + 1f, 1f);
			
			if(Vector3.Distance(ballBox.transform.localScale, targetScale) <= 0.05f){
				ballBox.transform.localScale = targetScale;
				scaleBallBox = false;
			} else if(ballBox.transform.localScale != targetScale){
				ballBox.transform.localScale = Vector3.Lerp(ballBox.transform.localScale, targetScale, Time.deltaTime*2f);
			} 
		}
	}

	void CalculateBounds(){
		minBounds.x = Mathf.Max(0, CenterX - SizeX * 0.5f);
		minBounds.y = Mathf.Max(0, CenterY - SizeY * 0.5f);

		maxBounds.x = Mathf.Min(springGrid.GetSideLength(), CenterX + SizeX * 0.5f);
		maxBounds.y = Mathf.Min(springGrid.GetSideLength(), CenterY + SizeY * 0.5f);

	}
}
