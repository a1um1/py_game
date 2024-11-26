# https://makefiletutorial.com/

run:
	python .

# https://github.com/CleanCut/green
test:
	green -vv test_*.py
	