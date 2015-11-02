using UnityEngine;
using System.Collections;

public enum NoteValues{
 	ronde, blanche, noire, croche, doubleCroche
}

[System.Serializable]
public class Clock : MonoBehaviour {
	
	public float bpm;
	public int num;
	public int sub;

	public int ticks = 0;
	[Space(20)]
	public int bar = 1;
	public int beat = 1;
	public int doubles = 1;

	[Space(20)]
	public float metroSpeed;
	public float barDur;


	// Use this for initialization
	public void Start () {
		metroSpeed = (60000 / sub) / bpm;
		barDur = (60000 / bpm) * num;

		InvokeRepeating("Tick", 0, metroSpeed * 0.001f);
	}
	
	// Update is called once per frame
	void Update () {
	
	}

	public void Tick(){
		ticks += 1;
		doubles = (doubles + 1) % sub;


		if(doubles == 0){
			beat = (beat + 1) % num;
		}

		if(beat == 0 && doubles == 0){
			bar += 1;
		}
	}
}
