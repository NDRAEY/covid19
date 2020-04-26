curl -s "https://www.worldometers.info/coronavirus/"\
 | grep "<title>" | sed "s/Coronavirus Update (Live): //g"\
  | sed "s+ Cases and + cases, +g" \
  | sed "s/ Deaths from COVID-19 Virus Pandemic - Worldometer/ deaths/g" | sed "s/<title>//g" | sed "s+</title>++g"
