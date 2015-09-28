using UnityEngine;
using System.Collections;

[System.Serializable]
public class SpringGridBlock {

	private GameObject block;
	public GameObject Block
	{ 
		get 
		{ 	
			return block; 	
		}
		set 
		{ 	
			block = value;	
		}
	}

	private GameObject anchor;
	public GameObject Anchor
	{ 
		get 
		{ 	
			return anchor; 	
		}
		set 
		{ 	
			anchor = value;	
			AnchorPos = value.transform.position;
			OldAnchorPos = value.transform.position;
		}
	}

	private Vector3 anchorPos;
	public Vector3 AnchorPos
	{ 
		get 
		{ 	
			return anchorPos; 	
		}
		set 
		{ 	
			anchorPos = value;	
		}
	}

	private Vector3 oldAnchorPos;
	public Vector3 OldAnchorPos
	{ 
		get 
		{ 	
			return oldAnchorPos; 	
		}
		set 
		{ 	
			oldAnchorPos = value;	
		}
	}
	
	private Rigidbody body;
	public Rigidbody Body
	{ 
		get 
		{ 	
			return body; 	
		}
		set 
		{ 	
			body = value;	
		}
	}

	private BoxCollider collider;
	public BoxCollider Collider
	{ 
		get 
		{ 	
			return collider; 	
		}
		set 
		{ 	
			collider = value;	
		}
	}

	private SpringJoint[] springs;
	public SpringJoint[] Springs
	{ 
		get 
		{ 	
			return springs; 	
		}
		set 
		{ 	
			springs = value;	
		}
	}

	private bool isRepositioning;
	public bool IsRepositioning
	{ 
		get 
		{ 	
			return isRepositioning; 	
		}
		set 
		{ 	
			isRepositioning = value;	
		}
	}

	private Vector3 targetPos;
	public Vector3 TargetPos
	{ 
		get 
		{ 	
			return targetPos; 	
		}
		set 
		{ 	
			targetPos = value;	
		}
	}


}
