#import numpy as np
import logging
#from mqt.qecc import CSSCode
from mqt.qecc.circuit_synthesis import gate_optimal_verification_circuit, heuristic_verification_circuit
from mqt.qecc.circuit_synthesis import CNOTCircuit, FaultyStatePrepCircuit

import qiskit.qasm2
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
)
logging.getLogger("mqt.qecc").setLevel(logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    
    if len(sys.argv)>2:    
        qasm = sys.argv[1]
        distance = int(sys.argv[2])
        # For the verificaiton circuit, the distance is used to determine the max number of errors, which is in turn used to determine the fault sets etc.
        method = sys.argv[3]
        
    try:
        non_ft_sp = qiskit.qasm2.loads(qasm)
        non_ft_sp = CNOTCircuit.from_qiskit_circuit(non_ft_sp, init_all = True)
        logger.info(f"Initialising FaultyStatePrepCircuit with max_errors = {(distance-1)//2}")
        non_ft_sp = FaultyStatePrepCircuit(non_ft_sp, (distance-1)//2, (distance-1)//2) #FaultyStatePrepCircuit(non_ft_sp, (distance-1)//2, (distance-1)//2) 
            
        if method == "optimal":
            ft_sp = gate_optimal_verification_circuit(non_ft_sp, verify_x_first=True) # first do Z-type measurements (to verify X errors)
        elif method == "heuristic":
            ft_sp = heuristic_verification_circuit(non_ft_sp, verify_x_first=True)
            
        print(qiskit.qasm2.dumps(ft_sp))
        sys.exit(0)
        
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()