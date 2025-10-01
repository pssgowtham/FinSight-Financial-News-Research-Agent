# CSS for chat layout
STYLES = """
<style>
.message { padding:10px 15px; margin:2px 0; border-radius:20px; max-width:75%; word-wrap:break-word; }
.user-msg { background-color:#DCF8C6; align-self:flex-end; margin-left:auto; color:black; }
.agent-msg { background-color:#E8E8E8; align-self:flex-start; margin-right:auto; color:black; }
.chat-end { float:left; clear:both; }
.input-fixed input[type="text"] { flex:1; padding:10px 15px; border-radius:20px; border:1px solid #ddd; outline:none; }
.input-fixed button { padding:10px 20px; border-radius:20px; border:1px solid #ddd; background-color:#4CAF50; color:white; font-weight:bold; cursor:pointer; }
.input-fixed button:hover { background-color:#45a049; }
.spinner-container { margin-top:5px; font-weight:bold; color:#555; }
</style>
"""
