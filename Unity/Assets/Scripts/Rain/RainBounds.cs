using UnityEngine;
using System.Collections;

public class RainBounds : MonoBehaviour {

	public int gridSize;

	public Vector2 size;
	public float SizeX {
		get {
			return size.x;
		}
		set {
			size.x = value;
			RangeSizeX = - SizeX + gridSize + 1;
		}
	}

	public float SizeZ {
		get {
			return size.y;
		}
		set {
			size.y = value;
			RangeSizeZ = -SizeZ + gridSize + 1;
		}
	}

	private Vector2 center;
	public float CenterX {
		get {
			return center.x;
		}
		set {
			center.x = value;
		}
	}

	public float CenterZ {
		get {
			return center.y;
		}
		set {
			center.y = value;
		}
	}

	private float rangeCenter;
	public float RangeCenter{
		get {
			return rangeCenter;
		}
		set {
			rangeCenter = value;
		}
	}


	public Vector2 rangeSize;
	public float RangeSizeX {
		get {
			return rangeSize.x;
		}
		set {
			rangeSize.x = value;
		}
	}

	public float RangeSizeZ {
		get {
			return rangeSize.y;
		}
		set {
			rangeSize.y = value;
		}
	}
}
