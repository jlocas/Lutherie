using UnityEngine;
using System.Collections;

public class RainBounds : MonoBehaviour {

	public float gridSize;
	public GameObject rangePrefab;
	public ParticleSystem particles;
	public float initSize;
	private GameObject rangeGO;


	private bool setScale = false;
	private Vector3 realSize; 		//size in the world, between 1 and grid size
	private Vector3 size; 			//controller value, between 0 and 1
	private Material mat;

	public float SizeX {
		get {
			return size.x;
		}
		set {
			size.x = value;
			realSize.x = size.x * (gridSize - 3) + 1; //+1 because we want a size of zero to cover 1 block

			RangeSizeX = -realSize.x + gridSize - 2;

			//reposition if out of bounds
			if(realCenter.x + realSize.x * 0.5f >= gridSize - 1 || realCenter.x - realSize.x * 0.5f <= 0){
				CenterX = center.x; //this works because center depends on rangeSize, which we set just above
			}

			setScale = true; 		//tells the update that we need to set the position because it changed
			this.enabled = true; 	//enables Update()
		}
	}

	public float SizeZ {
		get {
			return size.z;
		}
		set {
			size.z = value;
			realSize.z = size.z * (gridSize - 3) + 1; //+1 because we want a size of zero to cover 1 block

			RangeSizeZ = -realSize.z + gridSize - 2;

			//reposition if out of bounds
			if(realCenter.z + realSize.z * 0.5f >= gridSize - 1 || realCenter.z - realSize.z * 0.5f <= 0){
				CenterZ = center.z;	//this works because center depends on rangeSize, which we set just above
			}

			setScale = true; 		//tells the update that we need to set the position because it changed
			this.enabled = true; 	//enables Update()
		}
	}
	

	private bool setPos = false;
	private Vector3 realCenter;		//position in the world, between 0 and gridsize - 1
	private Vector3 center;			//controller value, between 0 and 1

	public float CenterX {
		get {
			return center.x;
		}
		set {
			center.x = value;
			realCenter.x = center.x * RangeSizeX + (realSize.x * 0.5f) - 0.5f + 1;

			setPos = true; 			//tells the update that we need to set the scale because it changed
			this.enabled = true; 	//enables Update()
		}
	}

	public float CenterZ {
		get {
			return center.z;
		}
		set {
			center.z = value;
			realCenter.z = center.z * RangeSizeZ + (realSize.z * 0.5f) - 0.5f + 1;

			setPos = true; 			//tells the update that we need to set the scale because it changed
			this.enabled = true; 	//enables Update()
		}
	}

	private float rangeCenter;
	public float RangeCenter{
		get {
			return rangeCenter;
		}
		set {
			rangeCenter = value;
			//SetRangePos(rangeCenter);
		}
	}


	public Vector3 rangeSize;
	public float RangeSizeX {
		get {
			return rangeSize.x;
		}
		set {
			rangeSize.x = value;
			//SetRangeScale(rangeSize);
		}
	}

	public float RangeSizeZ {
		get {
			return rangeSize.z;
		}
		set {
			rangeSize.z = value;
			//SetRangeScale(rangeSize);
		}
	}

	private void SetRangeScale(Vector3 s){
		rangeGO.transform.localScale = new Vector3(s.x, 1f, s.z);
	}

	private void SetRangePos(float p){
		rangeGO.transform.position = new Vector3(p, 0.5f, p);
	}

	public Vector3 GetBallPosition(){
		Vector3 pos = new Vector3(0f,50f,0f);
		pos.x = realCenter.x + Random.Range(realSize.x * -0.5f, realSize.x * 0.5f);
		pos.z = realCenter.z + Random.Range(realSize.z * -0.5f, realSize.z * 0.5f);
		return pos;
	}

	void Awake(){
		//for debugging
		//rangeGO = Instantiate(rangePrefab, new Vector3(rangeCenter, 0.5f, rangeCenter), Quaternion.identity) as GameObject;
		realSize = new Vector3(0f,1f,0f);
		realCenter = new Vector3(0f,0.5f,0f);
		mat = gameObject.GetComponent<MeshRenderer>().material;
	}




	/*
	 * ************************************************************************************************************************************************************
	 * ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	
	 * ************************************************************************************************************************************************************
	 * ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	ALL THE LERPS	
	 * ************************************************************************************************************************************************************
	 */

	public float lerpSpeed = 1f;
	public float lerpSnapDist = 0.1f;
	public bool isAppearing = false;
	public bool isDisappearing = false;
	public bool isHolding = false;
	public float opacityLerpTime = 1f;
	private float opacityLerpCurrentTime;
	public float opacityHoldTime = 2f;
	public float opacity;

	
	void LerpScale(){

		if(setScale){
			gameObject.transform.localScale = Vector3.Lerp(gameObject.transform.localScale, realSize, Time.deltaTime * lerpSpeed);
			mat.SetFloat("_Scale", ((realSize.x + realSize.z) * 0.5f) / (float)gridSize);
			
			if(Vector3.Distance(gameObject.transform.localScale, realSize) < lerpSnapDist){
				gameObject.transform.localScale = realSize;
				setScale = false;
			}
		}
	}

	void LerpPosition(){

		if(setPos){
			gameObject.transform.position = Vector3.Lerp(gameObject.transform.position, realCenter, Time.deltaTime * lerpSpeed);
			
			if(Vector3.Distance(gameObject.transform.position, realCenter) < lerpSnapDist){
				gameObject.transform.position = realCenter;
				setPos = false;
			}
		}
	}

	void LerpOpacity(){
			
		float lerpStart = opacity; //so the lerp doesnt start at 0 when opacity is greater than 0
		
		if((setPos || setScale) && !isAppearing){
			isAppearing = true;
			isDisappearing = false;
			isHolding = false;
			opacityLerpCurrentTime = 0f;	//timer 
		}
		
		//Apparition
		if(isAppearing){
			float t = 0f;
			opacityLerpCurrentTime += Time.deltaTime;
			t = Mathf.Clamp01(opacityLerpCurrentTime / opacityLerpTime);
			
			opacity = Mathf.Lerp(lerpStart, 1f, t);
			
			if(t == 1){
				isHolding = true;
				opacityLerpCurrentTime = 0f;
				isAppearing = false;
			}
		}
		
		if(isHolding){
			opacityLerpCurrentTime += Time.deltaTime;
			
			if(opacityLerpCurrentTime >= opacityHoldTime){
				opacityLerpCurrentTime = 0f;
				isDisappearing = true;
				isHolding = false;
			}
		}
		
		if(isDisappearing){
			float t = 0f;
			opacityLerpCurrentTime += Time.deltaTime;
			t = Mathf.Clamp01(opacityLerpCurrentTime / opacityLerpTime);
			
			opacity = Mathf.Lerp(1f, 0f, t);
			
			if(t == 1){
				opacityLerpCurrentTime = 0f;
				isDisappearing = false;
			}
		}
		
		mat.SetFloat("_DissolveAmount", opacity);

	}

	void Update(){

		LerpPosition();
		LerpScale();
		LerpOpacity();

		if(!setPos && !setScale && opacity == 0f){
				this.enabled = false; //disable Update() if setPos and setScale are false
		}
	}

	void Start(){
		SizeX = initSize;
		SizeZ = initSize;
		mat.SetFloat("_DissolveAmount", 0f);
	}
}
