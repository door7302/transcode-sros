# transcode-sros
Python script to transcode Nokia SROS config in flat mode


Description :
Allow to transcode a SROS config file collected by admin display-config in a flat config file
The only limitation is do not have 4 space characters in your description as indentation is 
made of 4 space characters

How to use:

python transcode-sros.py <my-sros-config-file>

Input : take your Nokia SROS config file

Ouput : create a flat config file named : flat-<my-sros-config-file>

Example. 

>> more mysros.cfg 
	Generated FRI NOV 25 08:15:08 2016 UTC

	exit all
	configure
	--------------------------------------------------
	echo "System Configuration"
	--------------------------------------------------
		system
			name "BOB"
			location "Bayonne Hardoy"
			chassis-mode d
			config-backup 6
			dns
			exit
			load-balancing
				l4-load-balancing
				lsr-load-balancing lbl-ip
			exit
			rollback
				rollback-location "cf3:/rollback"
				local-max-checkpoints 20
			exit
			snmp
				packet-size 9216
			exit
			time
				ntp
					server x.x.x.x prefer
					no shutdown
				exit
				sntp
					shutdown
				exit
				dst-zone CEST
					start last sunday march 02:00
					end last sunday october 03:00
				exit
				zone CET
			exit
			thresholds
				rmon
				exit
			exit
		exit
    
>> python trancode-sros.py mysros.cfg

	Flat config has been pushed in file: ./flat-mysros.cfg

>> more flat-mysros.cfg 
	configure system name "BOB"
	configure system location "Bayonne Hardoy"
	configure system chassis-mode d
	configure system config-backup 6
	configure system dns
	configure system load-balancing l4-load-balancing
	configure system load-balancing lsr-load-balancing lbl-ip
	configure system rollback rollback-location "cf3:/rollback"
	configure system rollback local-max-checkpoints 20
	configure system snmp packet-size 9216
	configure system time ntp server x.x.x.x prefer
	configure system time ntp no shutdown
	configure system time sntp shutdown
	configure system time dst-zone CEST start last sunday march 02:00
	configure system time dst-zone CEST end last sunday october 03:00
	configure system time zone CET
	configure system thresholds rmon
