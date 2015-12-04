using UnityEngine;
using System.Collections;

public class Ball : MonoBehaviour {

	public bool hasParticles = false;
	public GameObject particleContainer;
	public GameObject particles;
	private float force;
	public float Force 
	{
		get { return force; }  
		set { force = value; }
	}

	void OnTriggerEnter(Collider col)
	{
		GameObject newParticles;

		if(!hasParticles)
		{
			/*newParticles = Instantiate(particles, gameObject.transform.position, Quaternion.identity) as GameObject;
			hasParticles = true;*/
			//newParticles.transform.SetParent(particleContainer.transform);
		}
		col.attachedRigidbody.AddForce( MultiplyVelocity( gameObject.GetComponent<Rigidbody>().velocity, force) );
		Destroy(gameObject);
	}

	public void SetParticleContainer(GameObject contain)
	{
		particleContainer = contain;
	}

	private Vector3 MultiplyVelocity(Vector3 vel, float mul)
	{
		return new Vector3(vel.x * mul, vel.y * mul, vel.z * mul);
	}


}
