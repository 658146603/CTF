## `RSA`
```sh
# env
git clone https://github.com/ius/rsatool.git

git clone https://github.com/D001UM3/CTF-RSA-tool.git
    cd CTF-RSA-tool
    pip install -r "requirements.txt"

git clone https://github.com/Ganapati/RsaCtfTool.git
    cd RsaCtfTool
    pip install -r "requirements.txt"


sudo apt-get install libgmp-dev
sudo apt-get install libmpfr-dev
sudo apt-get install libmpc-dev

pip install libnum
pip install requests
pip install gmpy
pip install gmpy2
pip install pyasn1
pip install sagemath
pip install Crypto

# sh
python rsatool.py -p 23781539 -q 13574881
python rsatool.py -f PEM -o key.pem -n 13826123222358393307 -d 9793706120266356337
python rsatool.py -f DER -o key.der -p 4184799299 -q 3303891593
python solve.py -g --dumpkey --key /mnt/c/users/wcf/Desktop/Temp/ctf_solve/BUUCTF-RSA1/pub.key
python solve.py --verbose --private -i examples/wiener_attack.txt
python solve.py --verbose -k /mnt/c/Users/WCF/Desktop/Temp/ctf_solve/extremelyhardRSA/pubkey.pem --decrypt_int 54566...96086248

python low_e_rsahack.py
    c:5456...248
    e:3
    n:72105952...6787241

python solve.py -g --createpub -N your_modulus -e your_public_exponent -o public.pem

```

## ``