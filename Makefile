PY = python3

spds.gram-: parse_spds_gram-.py
	$(PY) $< 

spds.gram-.-: parse_spds_gram-.-.py
	$(PY) $< 
	
spds.gram+: parse_spds_gram+.py
	$(PY) $<

spds.gram+.-: parse_spds_gram+.-.py
	$(PY) $<

spds.euk: parse_spds_euk.py
	$(PY) $<

signalp.gram-: parse_signalp_gram-.py
	$(PY) $<

signalp.gram-.-: parse_signalp_gram-.-.py
	$(PY) $<

signalp.gram+: parse_signalp_gram+.py
	$(PY) $<

signalp.gram+.-: parse_signalp_gram+.-.py
	$(PY) $<

signalp.euk: parse_signalp_euk.py
	$(PY) $<

binary.kmeans: binary_classify/kmeans.py
	$(PY) $<
