# NeuralChain: Federated Learning on Decentralized Ledgers

Enabling privacy-preserving AI model training and deployment through smart contract-governed blockchain oracles.

This repository contains the code for NeuralChain, a framework designed to facilitate federated learning (FL) on decentralized ledgers. It addresses the critical need for privacy-preserving AI model training by leveraging the immutability and transparency of blockchain technology. NeuralChain utilizes smart contracts to govern the aggregation of model updates from distributed participants, ensuring that no single entity has access to the raw data used in training. Blockchain oracles, secured and verifiable, bridge the gap between on-chain smart contracts and off-chain machine learning processes, enabling secure and auditable AI model deployment. The system is designed to be robust against malicious actors and data poisoning attacks, thereby promoting trust and reliability in AI-driven applications.

The core goal of NeuralChain is to democratize access to AI model training and deployment while maintaining stringent privacy standards. It tackles the challenges of traditional centralized federated learning, where a single server can potentially compromise participant data. By distributing the aggregation process across a decentralized network and using smart contract-enforced protocols, NeuralChain eliminates the central point of failure and ensures that participants retain control over their sensitive data. This approach allows for the creation of AI models trained on diverse datasets without compromising the privacy of individual contributors, opening up new possibilities in domains such as healthcare, finance, and IoT.

NeuralChain offers a modular and extensible architecture, allowing developers to integrate existing machine learning frameworks and blockchain platforms. It provides tools for defining and deploying federated learning workflows, managing participant registration and authentication, and securely aggregating model updates. The framework includes components for data validation, outlier detection, and differential privacy implementation, further enhancing the robustness and trustworthiness of the trained models. By providing a secure and transparent environment for federated learning, NeuralChain empowers organizations to collaborate on AI projects while safeguarding the privacy of their data and intellectual property.

## Key Features

*   **Smart Contract-Governed Aggregation:** Decentralized aggregation of model updates is enforced by smart contracts deployed on a blockchain network. These contracts define the rules for participation, data validation, and model aggregation, ensuring transparency and auditability. Specific implementations use Solidity for Ethereum-compatible chains and may utilize libraries such as OpenZeppelin for security best practices.

*   **Blockchain Oracle Integration:** Secure and verifiable blockchain oracles are used to retrieve model parameters, trigger training rounds, and deploy trained models. These oracles rely on trusted execution environments (TEEs) or multi-party computation (MPC) to ensure data integrity and prevent manipulation of the model training process. We currently support Chainlink oracles and are exploring integration with other oracle providers.

*   **Privacy-Preserving Mechanisms:** Implementation of differential privacy (DP) techniques to protect the privacy of individual data contributions. DP adds controlled noise to the model updates, preventing inference of sensitive information. Specifically, we utilize Gaussian and Laplace mechanisms with dynamically adjustable privacy budgets (epsilon and delta).

*   **Modular and Extensible Architecture:** The framework is designed with modularity in mind, allowing developers to easily integrate different machine learning frameworks (e.g., TensorFlow, PyTorch) and blockchain platforms (e.g., Ethereum, Hyperledger Fabric). The codebase follows well-defined interfaces and supports plugin-based extensions.

*   **Data Validation and Anomaly Detection:** Incorporation of data validation and anomaly detection mechanisms to mitigate the risk of data poisoning attacks. These mechanisms analyze the statistical properties of the data contributions and flag any suspicious patterns or outliers. Algorithms include z-score analysis and isolation forests.

*   **Federated Averaging and Secure Aggregation:** Implementation of federated averaging algorithms for model aggregation, combined with secure aggregation protocols to protect the privacy of model updates during transmission. Secure aggregation utilizes homomorphic encryption or secure multi-party computation (MPC) to ensure that only the aggregated model is revealed.

*   **Automated Deployment and Monitoring:** Tools for automated deployment of smart contracts and oracles, as well as monitoring of the federated learning process. These tools provide real-time insights into the performance of the model, the status of the participants, and any potential issues that may arise. We use Prometheus and Grafana for monitoring and alerting.

## Technology Stack

*   **Python:** The primary programming language for implementing the federated learning algorithms, data processing pipelines, and client-side interactions.
*   **TensorFlow/PyTorch:** Machine learning frameworks used for training the AI models. The framework supports both TensorFlow and PyTorch, allowing developers to choose the framework that best suits their needs.
*   **Solidity:** Smart contract language for defining the rules for federated learning on the blockchain.
*   **Web3.py/Ether.py:** Python libraries for interacting with the Ethereum blockchain and deploying/interacting with smart contracts.
*   **Blockchain (Ethereum/Hyperledger Fabric):** The underlying decentralized ledger for managing participant registration, model aggregation, and secure oracle integration. The framework supports both permissioned and permissionless blockchain networks.
*   **Chainlink (or alternative oracle service):** A decentralized oracle network providing secure and reliable data feeds for the smart contracts.
*   **IPFS:** InterPlanetary File System for storing and retrieving large model files and data artifacts in a decentralized manner.

## Installation

1.  Clone the repository:
    git clone https://github.com/ezozu/NeuralChain.git
    cd NeuralChain

2.  Create a virtual environment:
    python3 -m venv venv
    source venv/bin/activate

3.  Install the required dependencies:
    pip install -r requirements.txt

4.  Install Ganache CLI for local Ethereum development (optional):
    npm install -g ganache-cli

## Configuration

1.  Set environment variables:

    Create a `.env` file in the root directory with the following variables:
    
    These variables are used to configure the connection to the blockchain, the account used for deploying and interacting with smart contracts, and the IPFS gateway for storing and retrieving model files.

2.  Configure the smart contract parameters in `contracts/NeuralChain.sol`:
    *   `_minParticipants`: Minimum number of participants required for a training round.
    *   `_aggregationThreshold`: Percentage of participants required to agree on the aggregated model.
    *   `_dataValidationThreshold`: Threshold for data validation checks.

## Usage

1.  Deploy the smart contracts to the blockchain using Remix IDE or Truffle. Ensure that you have configured the correct network and account settings.

2.  Start the federated learning process by calling the `startTrainingRound()` function in the smart contract. This will trigger the oracle to retrieve model parameters and initiate the training process.

3.  Participants can register to participate in the training round by calling the `registerParticipant()` function in the smart contract.

4.  Each participant trains the model on their local data and submits the model updates to the smart contract.

5.  The smart contract aggregates the model updates using federated averaging and publishes the aggregated model to IPFS.

6.  The oracle retrieves the aggregated model from IPFS and deploys it for inference.

Example Python code for interacting with the smart contract:


## Contributing

We welcome contributions to NeuralChain! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes, ensuring that the code is well-documented and follows the project's coding style.
4.  Write unit tests to verify the correctness of your changes.
5.  Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ezozu/NeuralChain/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to acknowledge the contributions of the open-source community to the various libraries and frameworks used in this project. We are grateful for the research and development efforts that have made federated learning and blockchain technology possible.