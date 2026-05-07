#import numpy as np
import logging
#from mqt.qecc import CSSCode
from mqt.qecc.circuit_synthesis import gate_optimal_verification_circuit#, heuristic_verification_circuit
from mqt.qecc.circuit_synthesis import CNOTCircuit, FaultyStatePrepCircuit

import qiskit.qasm2
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
)
logging.getLogger("mqt.qecc").setLevel(logging.INFO)

def main() -> None:
    
    if len(sys.argv)>1:    
        qasm = sys.argv[1]
        
    try:
        non_ft_sp = qiskit.qasm2.loads(qasm)
        non_ft_sp = CNOTCircuit.from_qiskit_circuit(non_ft_sp, init_all = True)
        non_ft_sp = FaultyStatePrepCircuit(non_ft_sp,1,1) # we fix max_x_errors = max_z_errors = 1, since we are working with distance=3 codes
        ft_sp = gate_optimal_verification_circuit(non_ft_sp)
        print(qiskit.qasm2.dumps(ft_sp))
        sys.exit(0)
        
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()