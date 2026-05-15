#import numpy as np
import logging
from mqt.qecc import CSSCode
from mqt.qecc.circuit_synthesis import gate_optimal_prep_circuit, heuristic_prep_circuit
#from mqt.qecc.circuit_synthesis import CNOTCircuit, FaultyStatePrepCircuit

import qiskit.qasm2
import sys
import numpy as np
import json

logging.basicConfig(
    level=logging.INFO,
    format="MQT.QECC Logging: %(asctime)s %(name)s %(levelname)s: %(message)s",
)
logging.getLogger("mqt.qecc").setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    
    if len(sys.argv)>3:  
        hx = np.array(json.loads(sys.argv[1]), dtype=np.int8)  
        distance = int(sys.argv[2])
        prep_method = sys.argv[3]
    try:
        code = CSSCode(np.transpose(hx), distance=distance)
        
        if prep_method == "optimal":
            encoding_circ = gate_optimal_prep_circuit(code, zero_state=True, max_timeout=16384) # default max_timeout is 3600s (1h);  will result in a total runtime of 1+2+4+...+16384 = 32767 ~ 9h (5 workers in parallel) 
        elif prep_method == "heuristic":
            encoding_circ = heuristic_prep_circuit(code, zero_state=True)
            
        print(qiskit.qasm2.dumps(encoding_circ.circ.to_qiskit_circuit())) # return the qasm string
        sys.exit(0)
        
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()