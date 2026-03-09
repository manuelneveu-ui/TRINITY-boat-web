import os

folder = r"pictures and video/Pictures and video/Pictures"
extensions = (".jpg", ".jpeg", ".png")  # converted images

tags = []
for name in sorted(os.listdir(folder)):
    if name.lower().endswith(extensions):
        path = f"{folder}/{name}"
        tags.append(f'  <img src="{path}" class="media-thumb" alt="">')

print("<div class=\"media-gallery\">")
print("\n".join(tags))
print("</div>")