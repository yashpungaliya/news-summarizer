import crawl


print("Fetching Articles...")
crawl.main()
print("......................\nAnalysing them...")
print("Generating a Summary...")
import analyseMat
analyseMat.analyse_all()

print("Done!")
