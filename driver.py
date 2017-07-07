import crawl


print("Fetching Articles...")
crawl.main()
print("......................\nAnalysing them...")
print("Generating a Summary...")
import analyse
analyse.analyse_all()

print("Done!")
