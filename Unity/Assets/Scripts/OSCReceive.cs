using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System;

public class OSCReceive : MonoBehaviour {

	/*
	 * 
	 * **************************************
	 * DO NOT CALL OSCHandler.Instance.Init() 
	 * IT IS CALLED IN OSCSender
	 * **************************************
	 * 
	 */

	Dictionary<string, ServerLog> servers;

	// Use this for initialization
	void Start () {
		servers = new Dictionary<string, ServerLog>();
	
	}
	
	// Update is called once per frame
	void Update () {
		OSCHandler.Instance.UpdateLogs();
		servers = OSCHandler.Instance.Servers;

		foreach(KeyValuePair<string, ServerLog> item in servers)
		{
			// If we have received at least one packet,
			// show the last received from the log in the Debug console
			if(item.Value.log.Count > 0) 
			{
				int lastPacketIndex = item.Value.packets.Count - 1;
				
				UnityEngine.Debug.Log(String.Format("SERVER: {0} ADDRESS: {1} VALUE 0: {2}", 
				                                    item.Key, // Server name
				                                    item.Value.packets[lastPacketIndex].Address, // OSC address
				                                    item.Value.packets[lastPacketIndex].Data[0].ToString())); //First data value


				switch(item.Value.packets[lastPacketIndex].Address)
				{
				case "springGrid/ballRate":
					Debug.Log(item.Value.packets[lastPacketIndex].Data[0]);
					break;
				}
			}
		}
	
	}
}
