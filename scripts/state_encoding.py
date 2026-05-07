#import numpy as np
import logging
from mqt.qecc import CSSCode
from mqt.qecc.circuit_synthesis import gate_optimal_prep_circuit, heuristic_prep_circuit
#from mqt.qecc.circuit_synthesis import CNOTCircuit, FaultyStatePrepCircuit

import qiskit.qasm2
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
)
logging.getLogger("mqt.qecc").setLevel(logging.INFO)

def main() -> None:
    
    if len(sys.argv)>1:    
        hx = sys.argv[1]
        
    try:
        # Need to pass read X stabilisers from julia script as npt.NDArray[np.int8] 
        
        code = CSSCode(hx)
        
        encoding_circ = gate_optimal_prep_circuit(code, zero_state=True, max_timeout=3600)
        #encoding_circ = heuristic_prep_circuit(code, zero_state=True)
                
        print(qiskit.qasm2.dumps(encoding_circ)) # return the qasm string
        sys.exit(0)
        
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()