#! /usr/bin/python
#
# Project Clearwater - IMS in the Cloud
# Copyright (C) 2015  Metaswitch Networks Ltd
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version, along with the "Special Exception" for use of
# the program along with SSL, set forth below. This program is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details. You should have received a copy of the GNU General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
#
# The author can be reached by email at clearwater@metaswitch.com or by
# post at Metaswitch Networks Ltd, 100 Church St, Enfield EN2 6BQ, UK
#
# Special Exception
# Metaswitch Networks Ltd  grants you permission to copy, modify,
# propagate, and distribute a work formed by combining OpenSSL with The
# Software, or a work derivative of such a combination, even if such
# copying, modification, propagation, or distribution would otherwise
# violate the terms of the GPL. You must comply with the GPL in all
# respects for all of the code used other than OpenSSL.
# "OpenSSL" means OpenSSL toolkit software distributed by the OpenSSL
# Project and licensed under the OpenSSL Licenses, or a work based on such
# software and licensed under the OpenSSL Licenses.
# "OpenSSL Licenses" means the OpenSSL License and Original SSLeay License
# under which the OpenSSL Project distributes the OpenSSL toolkit software,
# as those licenses appear in the file LICENSE-OPENSSL.

"""Script to check /etc/clearwater/config doesn't contain any unknown values
   that might be lost on migration."""

settings = []

with open('/etc/clearwater/config') as f:
	for line in f.readlines():
		if "=" in line and not line.startswith("#"):
			settings.append(line.split("=")[0])

possibilities = """
home_domain
sprout_hostname
bono_hostname
hs_hostname
hs_provisioning_hostname
ralf_hostname
cdf_identity
xdms_hostname
hss_hostname
signup_key
turn_workaround
smtp_smarthost
smtp_username
smtp_password
email_recovery_sender
ellis_api_key
icscf
scscf
homestead_provisioning_port
sas_server
reg_max_expires
sub_max_expires
upstream_hostname
upstream_port
sprout_rr_level
hss_mar_lowercase_unknown
enforce_user_phone
enforce_global_only_lookups
hs_listen_port
ralf_listen_port
default_session_expires
enum_server
enum_suffix
enum_file
icscf_uri
scscf_uri
additional_home_domains
hss_realm
billing_realm
diameter_timeout_ms
max_peers
num_http_threads
num_http_worker_threads
gemini_enabled
memento_enabled
max_call_list_length
call_list_store_ttl
memento_disk_limit
memento_threads
signaling_dns_server
target_latency_us
max_tokens
init_token_rate
min_token_rate
override_npdi
exception_max_ttl
check_destination_host
astaire_cpu_limit_percentage
sip_blacklist_duration
http_blacklist_duration
diameter_blacklist_duration
cassandra_hostname
ralf_secure_listen_port
hs_secure_listen_port
ellis_cookie_key
log_level
log_directory
num_pjsip_threads
num_worker_threads
upstream_connections
upstream_recycle_connections
authentication
num_http_threads
impu_cache_ttl
hss_reregistration_time
hss_port
snmp_ip
trusted_peers


local_ip
public_ip
public_hostname
chronos_hostname
signaling_namespace
etcd_cluster
node_idx
ralf_diameteridentity
hs_diameteridentity
alias_list
local_site_name
remote_site_name
""".split()

for option in settings:
	if option not in possibilities:
		print "WARNING: option {} exists in /etc/clearwater/config, but no migration code exists for this option".format(option)
