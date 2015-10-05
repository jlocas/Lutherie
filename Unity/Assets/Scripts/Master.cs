using UnityEngine;
using System.Collections;

public class Master : MonoBehaviour {

	public SpringGrid grid;

	public int gridLength;

	// Use this for initialization
	void Start () {
		gridLength = grid.GetSideLength();
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
