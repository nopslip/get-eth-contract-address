//node version: v9.10.0
//module versions:
//rlp@2.0.0
//keccak@1.4.0

const rlp = require('rlp');
const keccak = require('keccak');

var nonce = 0x10; //The nonce must be a hex literal!
// var sender = '0x6ac7ea33f8831ea9dcc53393aaa88b25a785dbf0'; //Requires a hex string as input!
var sender = '0xA1df472Fc3d9f9E5F54137D2878A3fA8adB63351';

var input_arr = [ sender, nonce ];
var rlp_encoded = rlp.encode(input_arr);

var contract_address_long = keccak('keccak256').update(rlp_encoded).digest('hex');

var contract_address = contract_address_long.substring(24); //Trim the first 24 characters.
console.log("contract_address: " + contract_address);