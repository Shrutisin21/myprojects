import argparse                                                                                                                                                                                                                                                                                                                                                                                                                                    
import time
import search
import pegSolitaireUtils

def main(args):
		
	flag = args.flag
	if not flag or flag == 1: 
		#Iterative Deepening Search
		tic = time.time()
		gameItrObject = pegSolitaireUtils.game(args.input)
		search.ItrDeepSearch(gameItrObject)
		toc = time.time()
		timeItr = toc - tic
		
		print ("Itr Deepening Search:")
		print ("Execution Time: " + str(timeItr))
		print ("Nodes Expanded: " + str(gameItrObject.nodesExpanded))
		print ("Trace: " + str(gameItrObject.trace)+ '\n')
	
	if not flag or flag == 2:
		#Astar with first heuristic
		tic = time.time()
		gameAOneObject = pegSolitaireUtils.game(args.input)
		search.aStarOne(gameAOneObject)
		toc = time.time()
		timeAOne = toc- tic
		
		print ("Astar One Search:")
		print ("Execution Time: " + str(timeAOne))
		print ("Nodes Expanded: " + str(gameAOneObject.nodesExpanded))
		print ("Trace: " + str(gameAOneObject.trace) + '\n'	)
	
	
	if not flag or flag == 3:
		#AStar with second Heuristic
		tic = time.time()
		gameATwoObject = pegSolitaireUtils.game(args.input)
		search.aStarTwo(gameATwoObject)
		toc = time.time()
		timeATwo = toc - tic
		
		print ("Astar Two Search:")
		print ("Execution Time: " + str(timeATwo))
		print ("Nodes Expanded: " + str(gameATwoObject.nodesExpanded))
		print ("Trace: " + str(gameATwoObject.trace))

	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="HomeWork One")
	parser.add_argument("--input",default="game.txt", type=str)
	parser.add_argument("--flag", type = int)
	args = parser.parse_args()
	main(args)
