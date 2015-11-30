using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class OSCReceive : MonoBehaviour {

	public ControlMapper controlMapper;
	Dictionary<string, ServerLog> servers = new Dictionary<string, ServerLog>();

	string oldAddress;
	float oldData;

	// Update is called once per frame
	void Update () {
		OSCHandler.Instance.UpdateLogs();
		servers = OSCHandler.Instance.Servers;

		foreach(KeyValuePair<string, ServerLog> item in servers){
			if(item.Value.log.Count > 0){
				int lastPacketIndex = item.Value.packets.Count - 1;

				string address = item.Value.packets[lastPacketIndex].Address;
				float data = (float)item.Value.packets[lastPacketIndex].Data[0];

				if(address != oldAddress || data != oldData){

					ToController(address, data);

					oldData = data;
					oldAddress = address;
				}

			}
		}
	}

	void ToController(string ad, float dat){
		switch(ad)
		{
		case "/controller/0":
			controlMapper.ctl0.Value = dat;
			controlMapper.ctl0.Send();
			break;
		case "/controller/1":
			controlMapper.ctl1.Value = dat;
			controlMapper.ctl1.Send();
			break;
		case "/controller/2":
			controlMapper.ctl2.Value = dat;
			controlMapper.ctl2.Send();
			break;
		case "/controller/3":
			controlMapper.ctl3.Value = dat;
			controlMapper.ctl3.Send();
			break;
		case "/controller/4":
			controlMapper.ctl4.Value = dat;
			controlMapper.ctl4.Send();
			break;
		case "/controller/5":
			controlMapper.ctl5.Value = dat;
			controlMapper.ctl5.Send();
			break;
		case "/controller/6":
			controlMapper.ctl6.Value = dat;
			controlMapper.ctl6.Send();
			break;
		case "/controller/7":
			controlMapper.ctl7.Value = dat;
			controlMapper.ctl7.Send();
			break;
		case "/controller/8":
			controlMapper.ctl8.Value = dat;
			controlMapper.ctl8.Send();
			break;
		case "/controller/9":
			controlMapper.ctl9.Value = dat;
			controlMapper.ctl9.Send();
			break;
		case "/controller/10":
			controlMapper.ctl10.Value = dat;
			controlMapper.ctl10.Send();
			break;
		case "/controller/11":
			controlMapper.ctl11.Value = dat;
			controlMapper.ctl11.Send();
			break;
		case "/controller/12":
			controlMapper.ctl12.Value = dat;
			controlMapper.ctl12.Send();
			break;
		case "/controller/13":
			controlMapper.ctl13.Value = dat;
			controlMapper.ctl13.Send();
			break;
		case "/controller/14":
			controlMapper.ctl14.Value = dat;
			controlMapper.ctl14.Send();
			break;
		case "/controller/15":
			controlMapper.ctl15.Value = dat;
			controlMapper.ctl15.Send();
			break;
		case "/controller/16":
			controlMapper.ctl16.Value = dat;
			controlMapper.ctl16.Send();
			break;
		case "/controller/17":
			controlMapper.ctl17.Value = dat;
			controlMapper.ctl17.Send();
			break;
		default:
			Debug.Log("OSCReceive: Unknown address");
			break;
		}
	}
}
