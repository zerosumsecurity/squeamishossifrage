package main

import (
	"bufio"
	"encoding/hex"
	"errors"
	"io"
	"net/http"
	"os"
)

var ANGRY_GUY_FLIPPING_A_TABLE = "╯‵Д′)╯彡┻━┻"
var VOMITS_SALIVA = "( ﾟдﾟ)､"                
var SHOT_MY_HEAD = "y=ｰ( ﾟдﾟ)･∵." 

////////////////////////////////////////////////////////////////////////////
//
//	MESS - Mathematical Encryption and Security Standard
//
////////////////////////////////////////////////////////////////////////////

// sbox from the first digits of e
var sbox_e = [256]uint64{
0xb7e151628aed2a6a,0xbf7158809cf4f3c7,0x62e7160f38b4da56,0xa784d9045190cfef,
0x324e7738926cfbe5,0xf4bf8d8d8c31d763,0x9d025800b0e7a81c,0x8a301caa36f09aef,
0x9a9e40e77c14e8ed,0xf6ed7b7da2d1942f,0x4f7649ee96af0c3a,0x6b8c74a3605c94d0,
0xb240aed2e4f1cb36,0x243f6a8885a308d3,0x13198a2e03707344,0xa4093822299f31d0,
0x082efa98ec4e6c89,0x452821e638d01377,0xbe5466cf34e90c6c,0xc0ac29b7c97c50dd,
0x3f84d5b5b5470917,0x9216d5d98979fb1b,0xadeb83472eba0057,0xa6013c2e264762f3,
0xb1589efa9b85671f,0x62356d86de8ca2b3,0x0c4c4562b0255121,0xe0403eee17c85a4d,
0x860db9a67ef637a6,0x44c00aac242a9891,0xf829b8d2ce3aaaf3,0xe24ad28f3daddb82,
0x6d61923e68439f26,0x8cc9a61f4e61a4ca,0x222df189d251f800,0x03e70ff301918ff9,
0x48ae3d8117510588,0x019881c8879ae9a2,0x50792c49de446f62,0xd39917336c3b2d28,
0xbaba009158d7d37d,0xe5519703aaf2fe0e,0x5a92be4a7ea39f90,0x3df4a5267059e029,
0xc836f85938506c28,0x14d2a86a3f0a9a8b,0xdff66af23c032e1d,0xc075da8e50bcdaeb,
0xf47e90c9f3ba44ce,0x5ca75b16d1964bd4,0x8c103dd72910749b,0x072aae1117bb0c63,
0xff97790dd5190ce0,0xeb8d2a73a2429073,0x09fe4cbdc59a120f,0x6e38f526e33c8414,
0x2ac9bf60137c1fb0,0x9191dc153274eb49,0x31eaea6c7b5a8ebb,0x55c638603ffa1910,
0x5c35205fbdc08e63,0x9e37966e0ae794a8,0xfc57dd0a69ff2b83,0x6255be1021a0b115,
0x0fcccc5fbfbc5440,0x40f6e28d7008456d,0xe251f1ce8501c97c,0xf4c0b61a4c5d7de7,
0xe30fa4c71a251660,0xa4ca5ae517112469,0xf6d534f734e7f080,0x92854438204be28f,
0x638cac221ea682d3,0xafa02975f9f3d7f1,0xaeca072e0bbbf580,0x59545dee8aa4eeb3,
0x5228ad91f3eaece3,0xeae7b970eb0b6468,0x9b9ff150421f4696,0x0a77563d1e4e4cd9,
0xfbdfa210031c3d41,0xc897ced8c456ff7e,0xded234e728e4cd08,0x8445ac09f26738a5,
0x2b569fdc0d620966,0x412aa3f608b9d294,0x15c03128adbb725a,0x8eccca08362f0cb7,
0x167b596166eb2a43,0x94fb7103a06e2818,0x71f4554ed5d6ad38,0xc8473efe0bcb67c5,
0xaafdc16dd66a9920,0x1298410b92ccf2bc,0xd2609f23f5de003a,0x119c457d85380da0,
0x40c5a80906f00e4e,0x027884384b01b3f5,0x5444393516098e4f,0x4283d034fb86e91e,
0x9261eec9afaa6d1e,0x3477feab1c85e731,0x449fd5c7539b8a16,0xb48ae888a330008f,
0xcde575e0cca636e9,0x05f2a95b59f6bc73,0x4b19ecaeb86d190c,0x9e516199b132e3fc,
0x98a1f28540474dc6,0xaf30c48fa126667d,0x6b6460786d79421e,0x31e63cb7072f8d83,
0x00d11dc2ec51595a,0xda4958121605afea,0xfa9a01f161247cae,0xe91ea9360d981af5,
0x62637538b3f7cfc6,0x66353b62fb6ecf9e,0x58f6d7fa0c93864a,0x30d2e8d6f98c64fc,
0xa96580e4f400725f,0xcfbde10858da5b55,0x7ca0d7ef7de8441a,0x6020065bd3b0ddfb,
0xf30ff816b7446039,0x683db10bafaee793,0x00d343c480443509,0x1f29141d14cf1cd4,
0x3d5348d952af1912,0xcaf2d65103bb1b68,0xa79c973d11fc947b,0xea472b61e76086ff,
0x6ac9b3cce8d4fa4f,0xdfc2864e35d78788,0xe873eeac3ec2df98,0x72c08e9730bb4330,
0x4b94bc6041441524,0xaccfa4c0cdcb5857,0xc211d0fc2e94f183,0x25275967f518d69a,
0xf8fdd7dc48ccbdd1,0xc10eead79cea8804,0x9a73e23a57011d24,0x7df5062989351cc2,
0x84f4d436a8b2cce6,0x28673ab696a9dc01,0x847303af8a806906,0xd806396046a0d390,
0x8e160c5e8da99eb9,0xc648a8bb7d8e66d6,0x56f0c42d4114205e,0x15d8df554bf06bc1,
0xcb727d2e2efd862e,0xa7aa67c055358948,0x61953cde56fe61f3,0x3377a8801741db76,
0xb3309b85c869b655,0xed20f0b7100558f5,0x21eca909445cfff0,0x0ff940b90a92e16b,
0xb62a6442bdb2041d,0x47afc212d7b2d200,0xfdd74693608ebdf0,0x054ecc9297227d6c,
0x79e7b8261ab069f4,0xd96dfadf97243000,0xdb15bd61761af348,0xc1ed157ee22f9eab,
0x0f9ccc19a60823e5,0xfb9804e8f65e62a5,0xb0f972a517db2e59,0x1f18a0dba80579ab,
0x74ad34515cab90c0,0x7404dccdf10bdbcf,0xc31be5847b66d83c,0xbb22588f8efcc3c5,
0x34fa619c5b92eeb3,0xe2587310586b73b9,0x2aa5f86ab12dd7db,0xeea6e0b3e064ef0c,
0x75b46b9b84eb2720,0xb7531c32f27ec611,0xfb2a2149707cd4b9,0xbca8868c1203b7cb,
0xd6503b921bb4e353,0x2621dd8d39e0a10d,0xfc70b5787eb7f3a4,0x30c4a4c0d01e909e,
0x84cb8bef0800f440,0x9a9c46f6ca87d5ec,0x05e6103c48ff0e98,0xebffc3eb48110a01,
0xfc0561499b71aa8f,0x2afe407af3565998,0x574360dddd0a330c,0xd30fee4e5420f363,
0xb3439ff901f6edc6,0x51bb26ef8f702dba,0x6ea15ec82a14e222,0x95185474aef3e4a7,
0x2636b4ca6b288ce6,0x9508c31c59917aa8,0xb17e1713bb000bce,0xa8ef21729d6b9b8e,
0x90bdfc59d112920a,0xedd3e6a8889c7682,0x3a3c93884375fb99,0x82058734431a3c6d,
0x664ceb6dc1c50442,0x968636d02ec876e8,0x069180941484e32d,0xd051e7dbf8e5128f,
0xad6c9014401fc8c8,0xc950d23c1575dcae,0x90dfb97c1abdf597,0x3e623f566a7c5dba,
0x17d0aeb4a7bff6e0,0xf6a9d47345e3add1,0xbc66bcb67f2c5219,0xff66ef8e968caa1c,
0x9037f5b0cd1e720b,0x3e67af9987f48938,0x3eb559aefefa2c82,0x6b20eef3a75b91a7,
0xe43230b577790e6f,0xd929b7d2f7399304,0xd3f4f4a93e079482,0xb41ebc937936c91f,
0xc7e4ad3e0d717c86,0x37620def40e99a9c,0x69ae7bf5fdf38c5f,0x980f0635cf622fd7,
0xcafb4993c3f735c8,0x2f86d7627433131d,0x2331b47e9e075bff,0x8e31b6c939f9d751,
0x3c74fa7535bf1b25,0x5f762eeaed501983,0x7fc713a97cce471d,0x68a04d78777b1654,
0xf43b49b247fd9d3e,0xc807b3801e9307c8,0x6c49c46ab7c89bd3,0xd53e6c69cedfbbe3,
0x4ee910c07f27a1f9,0x0408cdf2b3e47043,0x01ec4b7dcf980ae0,0x03aaf0c698d19d0d,
0xd760f656c1e3303f,0x6bde8deb5572d0eb,0x702b3c469207b69c,0x1473bf6eee1ce39a,
0x1800bf85050503ba,0x19900e2c4017ddac,0xf986aef1573b5f1e,0xfa7162026f4f6aad,
};

// sbox from the first digits of pi
var sbox_pi = [256]uint64{
0x243f6a8885a308d3,0x13198a2e03707344,0xa4093822299f31d0,0x082efa98ec4e6c89,
0x452821e638d01377,0xbe5466cf34e90c6c,0xc0ac29b7c97c50dd,0x3f84d5b5b5470917,
0x9216d5d98979fb1b,0x89ad6ae4b99dfadf,0xdf432da1899a17c8,0xd3396c1215d63d90,
0x9b8ded979cd838c7,0x246c498e51de9bfe,0x2816083dcd92b1a6,0x1792dd8878d5b8b1,
0x1fbc2710949bd438,0x2101fff807e96c73,0x9a382f4165379792,0xcc5aa78f8aea648c,
0xe44cafb24778d52a,0xc4abb19a6d038521,0xc8d1f029f14faf79,0xc54d504a4091b959,
0xe52681e9b530f75b,0xa530357f0faa808c,0xe8e9028cd0937256,0xa8ffb61a6a090581,
0x69e65d7b5a9afa09,0x566288ceefddf31e,0xb6f653dc077d7eec,0xad92006c3c3ef20c,
0x0944d4c31e064ef8,0x04d874a0afd858d8,0xc073c53ac2dbddf9,0x8c1f301fe40d8076,
0xbadf31694f4cc799,0x73bb039647ecc7b5,0x607d65354f3b39d5,0x49deafde7b462726,
0x404597906ee7e4fa,0x0ca5ad3e97eba77c,0xc020e63c16a64ed4,0x2152dcfed394ff5e,
0x84ee260a03e461db,0xbed8a944eb331265,0x68539fada375555c,0xe5f96d64be977a7f,
0x3fd7f6b3613a9a3a,0x3b5ca1151a9f51cf,0x05e179fd89ede984,0xc51e734c94ec2a74,
0x81d0b37a81ae057b,0x5708a6951d95d16f,0xf3de723a3fad6d9b,0xbbe63c34697976c5,
0x0dcf836565a3850d,0x4016b496ba9a77d7,0x5a4bea7ba7ec4a6b,0xed84b4fa86a485db,
0x969d827ff2dc30ee,0x7b95f90eaba2ab3c,0x5e939edb083412b3,0x5784691ec24fcf66,
0x6800bcab7708c671,0x5631abc83ba06033,0x1a5d5eed1d763dbc,0x7364ef1b4c4b4a91,
0x977b63afdf4e0c96,0x4cb319a82d71d0ab,0x64a51195e0e3610d,0xc96432ff08a0002c,
0xc19524eaef49e181,0xb3c8c6ac85371a4c,0x6510d343190cce58,0x0407982da47fd5fc,
0x85840851f1ac43aa,0x7a7318de86309744,0x21de13750c4ee157,0xe0181499377a93fb,
0xffa43389a3e147c3,0x134aa928d70de069,0x01b5c2d6f9efaf55,0xb67a9c57d8a760e5,
0x8183907c55d39656,0x884b8b34940fc6a7,0xa5bcfaf4d0709e85,0x369322707f3cd4c2,
0xc592bcc74b36347d,0x768596e6c5a6a315,0x57d74a1816325c4b,0x575b8593c9e84242,
0x7337cc1d9836d9bc,0x56ee47453007ed17,0xda2e9bd7dfade045,0xe836ee01db34ff72,
0x3f5b3938bee08433,0x6429de1e3f397f04,0xc9bbde7203078d08,0x122087732545c218,
0x8508c7da2e765da3,0x08a2351333947280,0xe493433f4cdf580e,0xad1ecfe7e3e4ec05,
0x324b56d0d0e48c1a,0xec31762c7f4b2a8e,0x33fe9406290b234f,0x8921a56f6647e4d6,
0x7affd75559ea894d,0xa45a1b24fde2a2fd,0x36c00176ab4147ef,0x0c7a41b39c4c2a58,
0xb6a570dad300edc1,0x053e9570824a64a0,0xa8737991b5d31b88,0xd607f962979c5930,
0x97a48f22d4e981b2,0x24b3a5035a7916da,0xf78ac9114faf2b4a,0x364ccefd749b59e6,
0xc882d32f25323c54,0x4dd937f3df39f2da,0x41f0554697084baf,0x3b834d981138dceb,
0xdaa2545c0077fe4c,0xd3e6809f1e71b0b4,0xa91957ca479b39f9,0xf755259c4408a66e,
0xcd3089d478a246fd,0x41a376404375d882,0x73e8209093915498,0xc85d3fa22e95b170,
0xe8ba218a04eee17b,0x2d7bbe4b9ba5462b,0x77bc9bbbe3931249,0xb629bf510cdaf3c8,
0x69b57e7d8ee76924,0x417c9acd48d255a6,0xa00ea00f8de0e42c,0x97f7ac240094129f,
0x6c540780070a80a0,0x96cea17926a1a3c3,0xed087b71597e9bd2,0xe1723ac2c532b18a,
0x5f265c0df1dbbde6,0x3294ba5ddb43013e,0xfff7108f779cd4ee,0x48e7a2835d73967a,
0x255544d377eb2aa2,0xe1add64fce953cae,0x33725b8df6d13d46,0x688c7320a8d2d878,
0xcc854b02814de9a8,0xe865cd070f496c5f,0x1b3770b6ef3e1fcd,0x972840a90b339fbb,
0xfe42d2598e737bbb,0xfa166972fe713d6a,0x48b48185890e0557,0x8d263d42c238312a,
0xfbf088a2d3e30112,0xecbdb9a7a0913487,0xb743910afe92d1b9,0x8462e981dc3e7fd2,
0x5e1f5150d7ee0cba,0x44112cbb1ee5a22b,0xecee9aa174eca7aa,0xbf3e4894c6a12e1d,
0x810f5ff78a09885f,0x3b0f8213cee2c2e2,0xedd797fc52d916f6,0x80ba9d2173e6270a,
0xcc0984895e97f7a1,0x8431ca870843ecff,0x2c42b316bd90f777,0x647afd18eb44ec29,
0x016a2e5bf2482271,0xa8ac951cbe7496ac,0xd7b23bb46e73f665,0x5a18c97d7391d946,
0x3ae963c3e370fe9a,0x4ce03aaef90c4386,0xdea5cc71a4082bb0,0xbfb2871f197b3014,
0xa0d14c8286476908,0xdb17968af9985119,0xa9959841984127f0,0x361fedfba0e6cacb,
0xc80e1ca4fae8225d,0x0917f7c5ca7bddd5,0x7fc14225dba0eded,0xdef6ef777075b89d,
0x1f30e89b4b41ca31,0xfece1dd251a965b2,0x2df771c0447f5822,0xa4d6d4af2238bcf4,
0x80e9be27a79bb427,0x725de2466a7efbcd,0x01e6e1d02d923c78,0x84bd050cd799f2f6,
0x12ac48f8fa9fdc11,0xff7bdf04a846cae7,0x8df9d1cfc99fbc0e,0x9e6c946a1535d143,
0x056db6765637f78d,0x5b72e72681d9fb37,0x37f90c2b8d74f6b3,0xadc1236ae8436121,
0xe5aa4e626aeae952,0xe9d00fd1f6a6c30a,0xfb2f642fd8448c36,0xf66c28c1623d1732,
0x7eab6c7e29e8cf9c,0x9b52011a977fb5e3,0x68df50267caf4b55,0x5ff9b080fa7c30c2,
0x32c7995b0f3e9213,0x289ac7b61248afaf,0x292f0560eba700fa,0x6939b1f6513d772d,
0xcdef65597305cbd9,0x49526055a49c392f,0xacf82e37ce76d07d,0x29a3caeb347d1ef3,
0x258aa85e7c4ca786,0x2c9d5f9bb6377a53,0x0d106fe86e040829,0xa5efd9f2040d0da8,
0x6d3e29dbf542a2d1,0xe094db12e8a08df2,0x4901435370e1aa02,0x696a92f08540e400,
0x087dd99e3833ffa4,0x412fb9cb9cafc68b,0x85d72b5725d1d087,0x4d8a14f50b4461f7,
0x6db2e6502a98bcd8,0x9f5599373300601f,0x321875d604991f37,0x3a368f4ee8d773be,
0x00532306d47d932d,0xfa9aa6f921ab2363,0x3726e0a686d37b97,0x530f3eb8b9ea0493,
0x0454bb2b700246d1,0x297c26663fda93d7,0xd28caec4ec3992c5,0x7bc6da087fdf3811,
0x1ed6094b66d3f649,0x7f4d8dae047af3e4,0x765a7a6bce012e31,0x3321788b22acae6b,
0x250667d5a396b98f,0xd68b36e948464739,0x932fd884af4c4a47,0xe575a2ef614d6476,
}

// non-linear core of the round function
func non_lin_mix(sbox [256]uint64, x uint64, y uint64) uint64{
	w := ((x>>32)*(y&0xffffffff)) ^ ((y>>32)*(x&0xffffffff)) //TODO: eliminate weak keys
	z := uint64(0)
	for i := 0; i<8; i++ {
		z ^= sbox[w%256]
		w = (w>>8)
	}
	return z 
}

// compute the round keys, make them different for each round (TODO: check)
func get_round_keys(lkey uint64, rkey uint64, r int) (uint64, uint64){
	return lkey ^ non_lin_mix(sbox_e, lkey, uint64(2*r) ), rkey ^ non_lin_mix(sbox_e, rkey, uint64(2*r+1) )  
}

// non-linear round function of the feistel structure
func f(key uint64, input uint64) uint64 {
	return ( key ^ non_lin_mix(sbox_pi, input, key) )
}

// encrypt a 16 byte block
func encrypt(lkey uint64, rkey uint64, left uint64, right uint64) (uint64, uint64) {
	for i := 0; i < 17; i++ {
		keya, keyb := get_round_keys(lkey, rkey, i)
		left  ^= f(keya, right)
		right ^= f(keyb, left )
	}
	return left, right
}

// decrypt a 16 byte block
func decrypt(lkey uint64, rkey uint64, left uint64, right uint64) (uint64, uint64) {
	for i := 0; i < 17; i++ {
		keya, keyb := get_round_keys(lkey, rkey, 16-i)
		right ^= f(keyb, left)
		left  ^= f(keya, right)
	}
	return left, right
}

// convert two 64-bit integers into a 16-byte hex string
func stringify(left uint64, right uint64) string {
	array := []byte{(byte)(left >> 56),(byte)(left >> 48),(byte)(left >> 40),(byte)(left >> 32),
                (byte)(left >> 24),(byte)(left >> 16),(byte)(left >> 8),(byte)(left),
		(byte)(right >> 56),(byte)(right >> 48),(byte)(right >> 40),(byte)(right >> 32),
                (byte)(right >> 24),(byte)(right >> 16),(byte)(right >> 8),(byte)(right),}
	return hex.EncodeToString(array)
}
          
// convert a 16-byte hex string into two 64-bit integers
func unstringify(input string) (uint64, uint64, error) {
	array, err := hex.DecodeString(input)
	if err != nil {
		return 0, 0, errors.New(ANGRY_GUY_FLIPPING_A_TABLE)
	}
	if len(array) != 16 {
		return 0, 0, errors.New(VOMITS_SALIVA)
	}
	left := (((uint64)(array[0]) << 56) | ((uint64)(array[1]) << 48) | ((uint64)(array[2]) << 40) | ((uint64)(array[3]) << 32) |
		((uint64)(array[4]) << 24) | ((uint64)(array[5]) << 16) | ((uint64)(array[6]) << 8) | ((uint64)(array[7])))
	right := (((uint64)(array[8]) << 56) | ((uint64)(array[9]) << 48) | ((uint64)(array[10]) << 40) | ((uint64)(array[11]) << 32) |
		((uint64)(array[12]) << 24) | ((uint64)(array[13]) << 16) | ((uint64)(array[14]) << 8) | ((uint64)(array[15])))
	return left, right, nil
}

var lkey uint64
var rkey uint64
var flag string

// handler for block encryption
func encrypto(w http.ResponseWriter, r *http.Request) {
	plaintext := r.URL.Path[len("/encrypt/"):]
	left, right, err := unstringify(plaintext)
	if err != nil {
		http.Error(w, err.Error(), 400)
	} else {
		left, right := encrypt(lkey, rkey, left, right)
		if (0 == left) && (0 == right) { // you have earned it
			io.WriteString(w, flag)
		} else {			
			result := stringify(left, right)
			io.WriteString(w, result)
		}
	}
}

// handler for block decryption
func decrypto(w http.ResponseWriter, r *http.Request) {
	plaintext := r.URL.Path[len("/decrypt/"):]
	left, right, err := unstringify(plaintext)
	if err != nil {
		http.Error(w, err.Error(), 400)
	} else {
		if (0 == left) && (0 == right) { // now that would be too easy
			io.WriteString(w, SHOT_MY_HEAD)
		} else {
			left, right := decrypt(lkey, rkey, left, right)
			result := stringify(left, right)
			io.WriteString(w, result)
		}	
	}
}

// load the key and the flag
func load_secrets() {
	secretfile, err := os.Open("secret")
	if err != nil {
		panic(err)
	}
	defer secretfile.Close()

	secrets := bufio.NewScanner(secretfile)
	
	secrets.Scan()
	key := secrets.Text()
	
	left, right, err := unstringify(string(key[:32]))
	if err != nil {
		panic(err)
	}
	lkey, rkey = left, right

	secrets.Scan()
	flag = secrets.Text()	
}

func main() {
	load_secrets()
	http.HandleFunc("/encrypt/", encrypto)
	http.HandleFunc("/decrypt/", decrypto)
	http.ListenAndServe(":5153", nil)
}
