# sbc_test_suite
A test suite for secure bootloader chain 
```
.
├── README.md
├── asset
│   ├── images
│   │   ├── image_corrupted_meta
│   │   ├── image_false_checksum
│   │   └── image_not_authentic
│   └── keys
│       ├── bad_key_1.pem
│       └── bad_key_2.pem
├── bootloaders
│   └── unsigned_2nd_bootloader
├── run_test_suite.py
├── singlestage.py
├── tc.py
├── twostage.py
└── utility.py
```

# How to run
```
./run_test_suite <test mdoe>
```

test mode can be `single_stage` or `two_stage`
