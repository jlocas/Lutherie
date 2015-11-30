using UnityEngine;
using System.Collections;


public class ControlMapper : MonoBehaviour {

	public SpringGrid grid;
	public Rain rain;

	public MidiController ctl0, ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, ctl8, ctl9, ctl10, ctl11, ctl12, ctl13, ctl14, ctl15, ctl16, ctl17;

	MidiController[] controls;

	void Start(){

		controls = new MidiController[18]{ctl0, ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, ctl8, ctl9, ctl10, ctl11, ctl12, ctl13, ctl14, ctl15, ctl16, ctl17};

		foreach(MidiController ctl in controls){
			ctl.Grid = grid;
			ctl.BallRain = rain;
		}
	}


}
