using UnityEngine;
using System.Collections;
using System.Diagnostics;

public enum CurrentConfig{
	School,
	Home
}

public class Master : MonoBehaviour {

	public SpringGrid grid;
	public CurrentConfig config;

	Process proc;
	ProcessStartInfo procsi;


	// Use this for initialization
	void Start () {
		proc = new Process();
		procsi = new ProcessStartInfo();
		string dir = "";

		/*if(config == CurrentConfig.Home){
			dir = @"W:\Projects\Lutherie\Pyo";
		} else if (config == CurrentConfig.School){
			dir = @"C:\Users\OPTIMUS\Documents\School\Projetlutherie\Pyo";
		}*/

		procsi.WorkingDirectory = @"W:\Projects\Lutherie\Pyo";

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
