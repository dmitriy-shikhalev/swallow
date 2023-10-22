import logging
from typing import Tuple

from .models import Channel, ChannelEnum, Message, Object, Ticket


logger = logging.getLogger(__name__)


def execute(message: Message) -> Tuple[Channel, Message]:
    """
    Execute one operator in ticket.
    """
    new_ticket = Ticket(
        ticket_id=message.ticket.ticket_id,
        units=message.ticket.units[1:],
    )

    try:
        result = message.ticket.units[0].operator(
            message.object
        )()
    except Exception as error:
        operator_name = message.ticket.units[0].operator.__name__
        logger.error('Error %s occur in operator %s', error, operator_name)
        error_message = Message(
            object=Object(
                kwargs={
                    'error': str(error),
                    'operator': operator_name,
                    'args': message.object,
                },
            ),
            ticket=new_ticket,
        )
        # Send to ERROR channel
        return ChannelEnum.ERROR.value, error_message

    new_message = Message(
        object=result,
        ticket=new_ticket
    )
    if not new_message.ticket.units:
        # Send to EXIT channel
        return ChannelEnum.EXIT.value, new_message

    # Send to a simple channel
    return (
        Channel(message.ticket.units[1].operator.__name__),
        new_message
    )
