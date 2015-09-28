using UnityEngine;
using System.Collections;

public class test : MonoBehaviour {

	public int tes;
	public int  _theVariable;

	public int TheVariable{
		get{return _theVariable;}
		set{
			_theVariable = value; 
			if ( _theVariable == 1){
				tes = _theVariable;
			}
		}
	}
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
