import json


def load_data():
    try:
        with open('youtube.txt','r') as file:
           return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file) 

def list_all_videos(videos):
    for index,video in enumerate(videos,start=1):
        print(f"{index},{video['name']} ,duration: {video['time']}")

def add_video(videos):
    name=input("enter video name: ")
    time = input("enter video time: ")
    videos.append({"name":name, "time":time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter a video no to be updated : "))
    if 1<= index <= len(videos):
        name = input("enter a new video name: ")
        time = input("enter a new time duration")
        videos[index-1] = {'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("invalid index selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input('enter the no u want to delete the video : '))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
         print("invalid index selected")



def main():
    videos = load_data()
    while True:
        print("YOUTUBE MANAGER | CHOOSE AN OPTION")
        print("1. List all youtube videos")
        print("2. Add a youtbe videos")
        print("3. Update a youtube videos details")
        print("4. Delete a youtube videos")
        print("5. Exit the app")
        choice = input("Enter your choice : ")
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('INVALID INPUT')

if __name__ == '__main__':
    main()

