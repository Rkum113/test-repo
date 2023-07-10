from git import Repo
username="Rkum113"
github_token="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"
owner="Rkum113"
def git_push(self):
    try:
        repo = Repo(f"/home/beehyv/Downloads/test-repo")
        repo.git.checkout('main')
        print(repo.git.status())
        repo.git.add(["test1.yaml", "test2.yaml"])
        print(repo.git.status())
        repo.index.commit(f"Test Release")
        remote_url = f"https://{username}:{github_token}@github.com/{owner}/test-repo.git"
        try:
            repo.create_remote(name="github_remote", url=remote_url)
        except Exception as e:
            print(e, "error while creating remote")
        origin = repo.remote("github_remote")
        origin.push()
    except Exception as e:
        print(e, "Some error occurred while pushing the code")