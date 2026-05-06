import numpy as np
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
)
logging.getLogger("mqt.qecc").setLevel(logging.INFO)
from mqt.qecc import CSSCode
from mqt.qecc.circuit_synthesis import gate_optimal_prep_circuit, heuristic_prep_circuit
from mqt.qecc.circuit_synthesis import gate_optimal_verification_circuit, heuristic_verification_circuit
from mqt.qecc.circuit_synthesis import VerificationNDFTStatePrepSimulator, CircuitLevelNoiseIdlingParallel

#import qiskit.qasm 
import qiskit.qasm2

import sys

from mqt.qecc.circuit_synthesis import CNOTCircuit, FaultyStatePrepCircuit

import matplotlib.pyplot as plt

def main() -> None:
    # hx = np.array(
    # [
    #     [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    #     [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0], 
    #     [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    #     [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    #     [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1], 
    # ],
    # dtype=np.int8,
    # )

    # hz = np.array(
    # [
    #     [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    #     [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    #     [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1], 
    #     [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
    #     [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    #     [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    # ],
    # dtype=np.int8,
    # )
    # trivariate_code = CSSCode(hx,hz,3)
    # #trivariate_code.Hx = hx
    # print(trivariate_code.Hz)
    # trivariate_code.Lx = np.array(
    #     [
    #         [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    #         [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    #     ])
    
    # trivariate_code.Lz = np.array(
    #     [
    #         [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
    #         [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    #     ])
    
    #trivariate_code.n = np.shape(hx)[1]
    #print(trivariate_code.n)
 
    
    
    #trivariate_code = CSSCode.from_code_name("Steane")
    #print(steane_code)
    #non_ft_sp = gate_optimal_prep_circuit(trivariate_code, zero_state=True, max_gates = 30, max_timeout=3600)
    #non_ft_sp = heuristic_prep_circuit(trivariate_code, zero_state=True)
    # I need to provide non_ft_step, which is a FaultyStatePrepCircuit object
    #print(non_ft_sp)
    #print(f"Non-FT encoding circuit, which was a CSS code now CNOT CIRcuit to FaultyStateRpep Circuit, has Z checks: {non_ft_sp.z_checks}")
    #non_ft_sp.circ.draw(output="mpl", initial_state=True)
    #plt.show()
    
#     qasm = """
#     OPENQASM 2.0;
#     include "qelib1.inc";
#     qreg q[12];
#     h q[4];
#     h q[3];
#     h q[2];
#     h q[1];
#     h q[0];
#     cx q[0],q[5];
#     cx q[2],q[5];
#     cx q[5],q[10];
#     cx q[1],q[6];
#     cx q[3],q[6];
#     cx q[2],q[7];
#     cx q[6],q[8];
#     cx q[8],q[5];
#     cx q[4],q[7];
#     cx q[7],q[8];
#     cx q[0],q[9];
#     cx q[2],q[11];
#     cx q[3],q[10];
#     cx q[3],q[11];
#     cx q[4],q[0];
#     """
#     qasm2 = """
#     OPENQASM 2.0;
# include "qelib1.inc";
# qreg q[18];
# h q[6];
# h q[5];
# h q[4];
# h q[3];
# h q[2];
# h q[1];
# h q[0];
# cx q[0],q[15];
# cx q[2],q[9];
# cx q[1],q[15];
# cx q[1],q[7];
# cx q[2],q[7];
# cx q[7],q[16];
# cx q[5],q[12];
# cx q[12],q[15];
# cx q[3],q[13];
# cx q[4],q[13];
# cx q[13],q[16];
# cx q[4],q[14];
# cx q[0],q[17];
# cx q[0],q[12];
# cx q[1],q[13];
# cx q[2],q[14];
# cx q[4],q[15];
# cx q[5],q[2];
# cx q[14],q[17];
# cx q[12],q[6];
# cx q[4],q[8];
# cx q[3],q[8];
# cx q[4],q[8];
# cx q[16],q[10];
# cx q[17],q[10];
# cx q[5],q[11];
# cx q[6],q[7];
# cx q[0],q[6];
# cx q[5],q[8];
# cx q[7],q[10];
# cx q[3],q[0];
# cx q[11],q[9];
# cx q[4],q[11];
# cx q[9],q[11];
# cx q[11],q[8];
# cx q[13],q[8];
# cx q[11],q[9];
# cx q[6],q[11];
# cx q[11],q[8];
# cx q[11],q[9];
# cx q[0],q[6];
#     """
    if len(sys.argv)>1:    
        qasm = sys.argv[1]
    try:
        non_ft_sp = qiskit.qasm2.loads(qasm)
    #print("HEEEERE", non_ft_sp)
        non_ft_sp = CNOTCircuit.from_qiskit_circuit(non_ft_sp, init_all = True)
    #print(non_ft_sp)
        non_ft_sp = FaultyStatePrepCircuit(non_ft_sp,1,1)
        ft_sp = gate_optimal_verification_circuit(non_ft_sp)#, only_first_layer=True)#, flag_first_layer=False)
        print(qiskit.qasm2.dumps(ft_sp))
        sys.exit(0)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

        
    #ft_sp = heuristic_verification_circuit(non_ft_sp)
    # ft_sp.draw(output="mpl", initial_state=True, fold=-1, scale=0.4)
    # plt.show()
    # p = 1e-3
    # noise = CircuitLevelNoiseIdlingParallel(p_tqg=p, p_sqg=p, p_init=p, p_meas=p, p_idle=p / 100)
    
    # print(f"Circuit is {non_ft_sp.circ.cnots}")

    # non_ft_simulator = VerificationNDFTStatePrepSimulator(
    #     non_ft_sp.circ, code=trivariate_code, zero_state=True
    # )
    # ft_simulator = VerificationNDFTStatePrepSimulator(
    #     ft_sp, code=trivariate_code, zero_state=True
    # )

    # pl_non_ft, ra_non_ft, _, _ = non_ft_simulator.logical_error_rate(noise, min_errors=10)
    # pl_ft, ra_ft, _, _ = ft_simulator.logical_error_rate(noise, min_errors=10)

    # print(f"Logical error rate for non-FT state preparation: {pl_non_ft}")
    # print(f"Logical error rate for FT state preparation: {pl_ft}")

if __name__ == "__main__":
    main()