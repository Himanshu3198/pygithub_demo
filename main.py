from  github import Github

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   g=Github("Enter your Token")
   # for repo in g.get_user().get_repos():
   #      print(repo.name)
   #      print(g.get_user().login)

repo_list=["website-template-using-html-css-bootstrap","ExpressJs-Routing-Demostration","Shopping-Store-UI","calculator-using-html-css-javascript"]
for i in range(len(repo_list)):
    print(repo_list[i])
    curr_repo="Himanshu3198/"+repo_list[i]
    repo = g.get_repo(curr_repo)
    file_path="jenkins.text"
    contents = repo.get_contents(file_path)
    print("before script "+contents.decoded_content.decode("utf-8"))
    new_content="this is updated content by script 4"
    repo.update_file(file_path,"update using pygithub",new_content,contents.sha)
    print("after script "+contents.decoded_content.decode("utf-8"))
