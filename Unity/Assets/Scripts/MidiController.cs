using UnityEngine;
using System.Collections;

public enum MappedParameter
{
	Rain1_XPos,
	Rain1_ZPos,
	Rain1_XSize,
	Rain1_ZSize,
	Rain1_BallForce,
	Rain1_Frequency,
	Rain1_SpawnBalls,
	Rain2_XPos,
	Rain2_ZPos,
	Rain2_XSize,
	Rain2_ZSize,
	Rain2_BallForce,
	Rain2_Frequency,
	Rain2_SpawnBalls,
	Springs_XSpring,
	Springs_YSpring,
	Springs_ZSpring,
	Springs_XDamp,
	Springs_YDamp,
	Springs_ZDamp,
	Springs_Reposition,
	Springs_FreezeEdges,
	Springs_RepositionNOW
}

public enum Form
{
	Lin,
	Exp
}

[System.Serializable]
public class MidiController {

	public MappedParameter parameter;
	public Form form;
	public float formArg;

	SpringGrid grid;
	public SpringGrid Grid
	{
		get{
			return grid;
		}
		set{
			grid = value;
		}
	}

	Rain rain1;
	public Rain BallRain1 {
		get{
			return rain1;
		}
		set{
			rain1 = value;
		}
	}

	Rain rain2;
	public Rain BallRain2 {
		get{
			return rain2;
		}
		set{
			rain2 = value;
		}
	}

	public float val;
	public float Value
	{
		get 
		{
			return val;
		}
		set
		{
			val = ApplyForm(value) * (maxVal - minVal) + minVal;
		}
	}

	public float minVal;
	public float maxVal;
	

	public void Send()	{
		switch(parameter)
		{
		case MappedParameter.Rain1_Frequency:
			break;
		case MappedParameter.Rain1_SpawnBalls:
			rain1.SpawnBalls = Value;
			break;
		case MappedParameter.Rain1_BallForce:
			rain1.BallForce = Value;
			break;
		case MappedParameter.Rain1_XPos:
			rain1.CenterX = Value;
			break;
		case MappedParameter.Rain1_XSize:
			rain1.SizeX = Value;
			break;
		case MappedParameter.Rain1_ZPos:
			rain1.CenterZ = Value;
			break;
		case MappedParameter.Rain1_ZSize:
			rain1.SizeZ = Value;
			break;

		case MappedParameter.Rain2_SpawnBalls:
			rain2.SpawnBalls = Value;
			break;
		case MappedParameter.Rain2_BallForce:
			rain2.BallForce = Value;
			break;
		case MappedParameter.Rain2_XPos:
			rain2.CenterX = Value;
			break;
		case MappedParameter.Rain2_XSize:
			rain2.SizeX = Value;
			break;
		case MappedParameter.Rain2_ZPos:
			rain2.CenterZ = Value;
			break;
		case MappedParameter.Rain2_ZSize:
			rain2.SizeZ = Value;
			break;

		case MappedParameter.Springs_FreezeEdges:
			grid.freezeEdges = Mathf.RoundToInt(Value) == 0 ? false : true;
			break;
		case MappedParameter.Springs_Reposition:
			grid.repositionBlocks = Mathf.RoundToInt(Value) == 0 ? false : true;
			break;
		case MappedParameter.Springs_RepositionNOW:
			grid.repositionNow = Mathf.RoundToInt(Value) == 0 ? false : true;
			break;
		case MappedParameter.Springs_XDamp:
			grid.damper.x = Value;
			break;
		case MappedParameter.Springs_XSpring:
			grid.spring.x = Value;
			break;
		case MappedParameter.Springs_YDamp:
			grid.damper.y = Value;
			break;
		case MappedParameter.Springs_YSpring:
			grid.spring.y = Value;
			break;
		case MappedParameter.Springs_ZDamp:
			grid.damper.z = Value;
			break;
		case MappedParameter.Springs_ZSpring:
			grid.spring.z = Value;
			break;
		}
	}

	float ApplyForm(float v){
		switch(form)
		{
		case Form.Lin:
			break;
		case Form.Exp:
			v = Mathf.Pow(formArg, v);
			break;
		}
		return v;
	}

}
