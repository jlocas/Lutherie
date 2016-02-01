using UnityEngine;
using System.Collections;


public class ControlMapper : MonoBehaviour {

	public SpringGrid grid;
	public Rain rain1;
	public Rain rain2;

	public MidiController ctl0, ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, ctl8, ctl9, ctl10, ctl11, ctl12, ctl13, ctl14, ctl15, ctl16, ctl17, ctl18, ctl19, ctl20, ctl21, ctl22, ctl23, ctl24, ctl25, ctl26;

	MidiController[] controls;

	void Start(){

		controls = new MidiController[27]{ctl0, ctl1, ctl2, ctl3, ctl4, ctl5, ctl6, ctl7, ctl8, ctl9, ctl10, ctl11, ctl12, ctl13, ctl14, ctl15, ctl16, ctl17, ctl18, ctl19, ctl20, ctl21, ctl22, ctl23, ctl24, ctl25, ctl26};

		foreach(MidiController ctl in controls){
			ctl.Grid = grid;
			ctl.BallRain1 = rain1;
			ctl.BallRain2 = rain2;

		}
	}


}
