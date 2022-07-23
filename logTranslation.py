import discord

def translateLog(entry : discord.AuditLogEntry, action : discord.AuditLogAction):
    actionList = {
            discord.AuditLogAction.guild_update:                            f'{entry.target} 항목을 변경했습니다.\n',
            discord.AuditLogAction.channel_create:                          f'{entry.target} 채팅 채널을 생성했습니다.\n',
            discord.AuditLogAction.channel_update:                          f'{entry.target} 항목을 변경했습니다.\n',
            discord.AuditLogAction.channel_delete:                          f'{entry.target} 항목을 제거했습니다.\n',
            discord.AuditLogAction.overwrite_create:                        f'{entry.target}에 채널 우선 설정 규칙을 생성했습니다.\n',
            discord.AuditLogAction.overwrite_update:                        f'{entry.target}에 채널 우선 설정 규칙을 업데이트했습니다.\n',
            discord.AuditLogAction.overwrite_delete:                        f'{entry.target}에 채널 우선 설정 규칙을 제거했습니다.\n',
            discord.AuditLogAction.kick:                                    f'{entry.target}님을 추방했습니다.\n',
            discord.AuditLogAction.member_prune:                            f'활동하지 않는 멤버 {entry.extra}명을 정리했습니다.\n',
            discord.AuditLogAction.ban:                                     f'{entry.target}님을 차단했습니다.\n',
            discord.AuditLogAction.unban:                                   f'{entry.target}님의 차단을 해제했습니다.\n',
            discord.AuditLogAction.member_update:                           f'{entry.target} 항목을 업데이트했습니다.\n',
            discord.AuditLogAction.member_role_update:                      f'{entry.target}님의 역할을 업데이트했습니다.\n',
            discord.AuditLogAction.member_move:                             f'사용자 {entry.extra}명을 {entry.extra}로 옮겼습니다.\n',
            discord.AuditLogAction.member_disconnect:                       f'사용자 {entry.extra}명의 음성 연결을 끊었습니다.\n',
            discord.AuditLogAction.bot_add:                                 f'{entry.target}님을 서버에 추가했습니다.\n',
            discord.AuditLogAction.thread_create:                           f'{entry.target} 스레드를 생성했습니다.\n', 
            discord.AuditLogAction.thread_update:                           f'{entry.target} 스레드를 변경했습니다.\n',  
            discord.AuditLogAction.thread_delete:                           f'{entry.target} 스레드를 삭제했습니다.\n', 
            discord.AuditLogAction.role_create:                             f'{entry.target} 역할을 생성했습니다.\n',
            discord.AuditLogAction.role_update:                             f'{entry.target} 역할을 업데이트했습니다.\n',
            discord.AuditLogAction.role_delete:                             f'{entry.target} 역할을 삭제했습니다.\n',
            discord.AuditLogAction.invite_create:                           f'{entry.target} 초대 코드를 생성했습니다.\n',
            discord.AuditLogAction.invite_update:                           f'{entry.target} 초대 코드를 업데이트했습니다.\n',
            discord.AuditLogAction.invite_delete:                           f'{entry.target} 초대 코드를 삭제했습니다.\n',
            discord.AuditLogAction.webhook_create:                          f'{entry.target} 웹후크를 생성했습니다.\n',
            discord.AuditLogAction.webhook_update:                          f'{entry.target} 웹후크를 업데이트했습니다.\n',
            discord.AuditLogAction.webhook_delete:                          f'{entry.target} 웹후크를 삭제했습니다.\n',
            discord.AuditLogAction.emoji_create:                            f'{entry.target} 이모티콘을 생성했습니다.\n',
            discord.AuditLogAction.emoji_update:                            f'{entry.target} 이모티콘을 업데이트했습니다.\n',
            discord.AuditLogAction.emoji_delete:                            f'{entry.target} 이모티콘을 삭제했습니다.\n',
            discord.AuditLogAction.message_delete:                          f'{entry.extra}에서 {entry.target}님이 쓴 메세지 {entry.extra}개를 삭제했습니다.\n',
            discord.AuditLogAction.message_bulk_delete:                     f'{entry.target}에서 메세지 {entry.extra}개를 삭제했습니다.\n',
            discord.AuditLogAction.message_pin:                             f'{entry.extra}에서 {entry.target}님이 쓴 메세지를 고정했습니다.\n',
            discord.AuditLogAction.message_unpin:                           f'{entry.extra}에서 {entry.target}님이 쓴 메세지를 고정 해제했습니다.\n',
            discord.AuditLogAction.integration_create:                      f'{entry.target} 연동을 생성했습니다.\n',
            discord.AuditLogAction.integration_update:                      f'{entry.target} 연동을 업데이트했습니다.\n',
            discord.AuditLogAction.integration_delete:                      f'{entry.target} 연동을 삭제했습니다.\n', 
            discord.AuditLogAction.sticker_create:                          f'{entry.target} 스티커를 만들었습니다.\n', 
            discord.AuditLogAction.sticker_update:                          f'{entry.target} 스티커를 업데이트했습니다.\n', 
            discord.AuditLogAction.sticker_delete:                          f'{entry.target} 스티커를 삭제했습니다.\n', 
            discord.AuditLogAction.stage_instance_create:                   f'{entry.target} 무대 채널을 생성했습니다.\n', 
            discord.AuditLogAction.stage_instance_update:                   f'{entry.target} 항목을 변경했습니다.\n', 
            discord.AuditLogAction.stage_instance_delete:                   f'{entry.target} 항목을 제거했습니다.\n', 
            discord.AuditLogAction.scheduled_event_create:                  f'{entry.target} 이벤트를 예약했습니다.\n', 
            discord.AuditLogAction.scheduled_event_update:                  f'예약된 이벤트인 {entry.target}을(를) 업데이트했습니다.\n', 
            discord.AuditLogAction.scheduled_event_delete:                  f'예정된 이벤트인 {entry.target}을(를) 취소했습니다.\n', 
            # discord.AuditLogAction.application_command_permission_update:   f'', 
        }

    return actionList[action]