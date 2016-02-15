using UnityEngine;
using System.Collections;

public class Ball_2 : MonoBehaviour {

	public bool hasParticles = false;
	private bool sentData = false;
	public GameObject particleContainer;
	public GameObject particles;
	public OSCSender sender;
	private float force;
	public float Force 
	{
		get { return force; }  
		set { force = value; }
	}

	void OnTriggerEnter(Collider col)
	{
		if(col.tag != "Ball"){
			/*GameObject newParticles;

			if(!hasParticles)
			{
				newParticles = Instantiate(particles, gameObject.transform.position, Quaternion.identity) as GameObject;
			hasParticles = true;
				newParticles.transform.SetParent(particleContainer.transform);
			}*/
			col.attachedRigidbody.AddForce( MultiplyVelocity( gameObject.GetComponent<Rigidbody>().velocity, force) );

			if(!sentData){
				sender.SendBall2Hit((int)gameObject.transform.position.x, (int)gameObject.transform.position.z);
				sentData = true;
			}
			Destroy(gameObject);
		}
	}

	public void SetParticleContainer(GameObject ctr)
	{
		particleContainer = ctr;
	}

	private Vector3 MultiplyVelocity(Vector3 vel, float mul)
	{
		return new Vector3(vel.x * mul, vel.y * mul, vel.z * mul);
	}


}
