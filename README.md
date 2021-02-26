# PrivacyGuard

#### PrivacyGuard: Enhancing Smart Home User Privacy
Keyang Yu, Qi Li, Dong Chen, Mohammad Rahman, and Shiqiang Wang

The Internet of Things (IoT) devices have been increasingly deployed
in smart homes and smart buildings to monitor and control
their environments. The Internet traffic data produced by these IoT
devices are collected by Internet Service Providers (ISPs) and IoT device
manufacturers, and often shared with third-parties to maintain
and enhance user services. Unfortunately, extensive recent research
has shown that on-path adversaries can infer and fingerprint users’
sensitive privacy information such as occupancy and user in-home
activities by analyzing IoT network traffic traces. Most recent approaches
that aim at defending against these malicious IoT traffic
analytics can not sufficiently protect user privacy with reasonable
traffic overhead. In particular, many approaches did not consider
practical limitations, e.g., network bandwidth, maximum package
injection rate or actual user in-home behavior in their design.
To address this problem, we design a new low-cost, open-source
user “tunable” defense system—PrivacyGuard that enables users
to significantly reduce the private information leaked through IoT
device network traffic data, while still permitting sophisticated data
analytics or control that is necessary in smart home management.
In essence, our approach employs intelligent deep convolutional
generative adversarial networks (DCGANs)-based IoT device traffic
signature learning, long short-term memory (LSTM)-based artificial
traffic signature injection, and partial traffic reshaping to obfuscate
private information that can be observed in IoT device traffic
traces. We evaluate PrivacyGuard using IoT network traffic traces
of 31 IoT devices from 5 smart homes. We find that PrivacyGuard
can effectively prevent a wide range of state-of-the-art machine
learning-based and deep learning-based occupancy and other 9 user
in-home activity detection attacks. We release the source code and
datasets of PrivacyGuard to IoT research community.

## Datasets

To download data: [Download (TBA)](http://50.19.41.57/).
