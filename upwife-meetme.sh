#!/bin/bash

random_number() {
  WAIT_TIME=$[ $RANDOM % 5 + 1 ]
}

timestamp() {
	echo -n $(echo upwife)\|$(date +"%T")\| # current time
}

log() {
  timestamp
  echo $@
}

send_wife_retrieval_payload() {
  log targeting potential wife
  adb shell input tap 459 1163
  log sent payload
}

prepare_for_next_potential_wife() {
  log preparing for next wife
  random_number
  sleep $WAIT_TIME
}


for (( ; ; ))
do
  send_wife_retrieval_payload
  prepare_for_next_potential_wife
done

