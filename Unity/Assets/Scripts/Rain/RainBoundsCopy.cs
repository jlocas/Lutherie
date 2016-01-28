using UnityEngine;
using System.Collections;

public class RainBoundsCopy : MonoBehaviour {

	public float gridSize;
	public GameObject rangePrefab;
	private GameObject rangeGO;

	private Vector3 startSize;
	private Vector3 startPos;

	public bool lerpSize = false;
	public bool lerpPos = false;

	//for scale and pos lerps
	private float slDistance = 0f;
	private float plDistance = 0f;

	private float lerpSpeed = 0.5f;


	public Vector3 size;
	private Vector3 realSize;
	public float SizeX {
		get {
			return size.x;
		}
		set {
			startSize.x = realSize.x; // for lerp
			size.x = value;
			realSize.x = size.x * (gridSize - 1) + 1; //+1 because we want a size of zero to cover 1 block

			RangeSizeX = -realSize.x + gridSize;

			if(realCenter.x + realSize.x * 0.5f >= gridSize - 1 || realCenter.x - realSize.x * 0.5f <= 0){
				CenterX = center.x;
				//SetPos(realCenter);
			}

			slDistance = Vector3.Distance(gameObject.transform.localScale, realSize);
			lerpSize = true;
		}
	}

	public float SizeZ {
		get {
			return size.z;
		}
		set {
			startSize.z = realSize.z; // for lerp
			size.z = value;
			realSize.z = value * (gridSize - 1) + 1; //+1 because we want a size of zero to cover 1 block

			RangeSizeZ = -realSize.z + gridSize;

			if(realCenter.z + realSize.z * 0.5f >= gridSize - 1 || realCenter.z - realSize.z * 0.5f <= 0){
				CenterZ = center.z;
				//SetPos(realCenter);
			}

			slDistance = Vector3.Distance(gameObject.transform.localScale, realSize);
			lerpSize = true;
		}
	}
	

	public Vector3 center;
	private Vector3 realCenter;
	public float CenterX {
		get {
			return center.x;
		}
		set {
			startPos.x = center.x;
			center.x = value;
			realCenter.x = value * RangeSizeX + (realSize.x * 0.5f) - 0.5f;

			plDistance = Vector3.Distance(gameObject.transform.position, realCenter);
			lerpPos = true;
		}
	}

	public float CenterZ {
		get {
			return center.z;
		}
		set {
			startPos.z = center.z;
			center.z = value;
			realCenter.z = value * RangeSizeZ + (realSize.z * 0.5f) - 0.5f;

			plDistance = Vector3.Distance(gameObject.transform.position, realCenter);
			lerpPos = true;
		}
	}

	private float rangeCenter;
	public float RangeCenter{
		get {
			return rangeCenter;
		}
		set {
			rangeCenter = value;
			SetRangePos(rangeCenter);
		}
	}


	public Vector3 rangeSize;
	public float RangeSizeX {
		get {
			return rangeSize.x;
		}
		set {
			rangeSize.x = value;
			SetRangeScale(rangeSize);
		}
	}

	public float RangeSizeZ {
		get {
			return rangeSize.z;
		}
		set {
			rangeSize.z = value;
			SetRangeScale(rangeSize);
		}
	}

	private void SetRangeScale(Vector3 s){
		rangeGO.transform.localScale = new Vector3(s.x, 1f, s.z);
	}

	private void SetRangePos(float p){
		rangeGO.transform.position = new Vector3(p, 0.5f, p);
	}

	private void UpdateScale(){
		if(lerpSize){
			float t = Mathf.SmoothStep(0f, 1f, slDistance / Vector3.Distance(gameObject.transform.localScale, realSize));

			gameObject.transform.localScale = realSize;

			if(Vector3.Distance(gameObject.transform.localScale, realSize) == 0f){
				lerpSize = false;
			}
		}
	}

	private void UpdatePos(){
		if(lerpPos){
			float t = Mathf.SmoothStep(0f, 1f, plDistance / Vector3.Distance(gameObject.transform.position, realCenter));
			
			gameObject.transform.position = realCenter;
			
			if(Vector3.Distance(gameObject.transform.position, realCenter) == 0f){
				lerpSize = false;
			}
		}
	}

	void Awake(){
		rangeGO = Instantiate(rangePrefab, new Vector3(rangeCenter, 0.5f, rangeCenter), Quaternion.identity) as GameObject;
		startSize = new Vector3(0f,1f,0f);
		startPos = new Vector3(0f,0.5f,0f);
		realSize = new Vector3(0f,1f,0f);
		realCenter = new Vector3(0f,0.5f,0f);

		CenterX = 0.5f;
		CenterZ = 0.5f;
		SizeX = 1;
		SizeZ = 1;
	}

	void Update(){
		UpdateScale();
		UpdatePos();
	}
}
