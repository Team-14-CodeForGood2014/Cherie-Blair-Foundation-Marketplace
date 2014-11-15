<?php
/**
 * User: svchost
 * Date: 14.5.11
 * Time: 14:33
 */

$json = <<<EOT
{
	"success":	1,
	"data":
		[
			{
				"unitvalue":	3,
				"unit":	"kilos",
				"keyword": "butter",
				"meName": "Bob",
				"region": "Europe",
				"carrier": "DHL",
				"qualitymatch": 0
			},
			{
				"unitvalue":	7,
				"unit":	"kilos",
				"keyword": "butter",
				"meName": "Kris",
				"region": "Europe",
				"carrier": "Express",
				"qualitymatch": 0
			},
			{
				"unitvalue":	2,
				"unit":	"kilos",
				"keyword": "butter",
				"meName": "Carlos",
				"region": "Europe",
				"carrier": "DHL",
				"qualitymatch": 1
			},
			{
				"unitvalue":	3,
				"unit":	"kilos",
				"keyword": "butter",
				"meName": "William",
				"region": "Asia",
				"carrier": "DHL",
				"qualitymatch": 1
			},
			{
				"unitvalue":	5,
				"unit":	"kilos",
				"keyword": "butter",
				"meName": "David",
				"region": "Europe",
				"carrier": "DHL",
				"qualitymatch": 1
			}
		]
}
EOT;


//$deunitvaluede = json_deunitvaluede($json, true);

if (json_last_error() != JSON_ERROR_NONE) {
	exit (json_enunitvaluede(array("success" => 0, "error" => "wrong json!")));
}

//print_r($deunitvaluede);

exit($json);

?>