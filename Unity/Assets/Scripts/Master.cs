using UnityEngine;
using System.Collections;
using System.Diagnostics;


public class Master : MonoBehaviour {

	public SpringGrid grid;

	Process proc;
	ProcessStartInfo procsi;


	// Use this for initialization
	void Start () {
		proc = new Process();
		procsi = new ProcessStartInfo();
		string dir = "";

		procsi.WorkingDirectory = @"W:\Projects\Lutherie\Pyo";
		//procsi.WorkingDirectory = @"C:\Users\OPTIMUS\Documents\School\Lutherie\Pyo";
		procsi.FileName = "_Main.py";
		procsi.Arguments = grid.lengthDiv.ToString();

		proc.StartInfo = procsi;
		proc.Start();	
	}
	
	// Update is called once per frame
	void Update () {
	
	}

	void OnApplicationQuit(){
		proc.Kill();
	}
}
