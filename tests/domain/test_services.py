from swallow.domain import models, services


class OperatorTest(models.AbstractOperator):
    def __call__(self, object: models.Object):
        return object.args[0] * 3,


class OperatorTest2(models.AbstractOperator):
    def __call__(self, object):
        ...


class OperatorTestError(models.AbstractOperator):
    def __call__(self, object):
        raise Exception('Test error occur!')


def test_execute_exit():
    ticket = models.Ticket(
        ticket_id=models.TicketID('test ticket id'),
        units=[
            models.Unit(
                channel=models.Channel('test channel'),
                operator=OperatorTest()
            )
        ]
    )
    message = models.Message(
        models.Object(args=(3, )),
        ticket=ticket
    )

    channel, message = services.execute(message)

    assert channel == models.ChannelEnum.EXIT.value
    assert message.object == (9, )
    assert message.ticket == models.Ticket(
        ticket_id=models.TicketID('test ticket id'),
        units=[],
        num=0,
        is_last=True
    )


def test_execute_error():
    ticket = models.Ticket(
        ticket_id=models.TicketID('test ticket id'),
        units=[
            models.Unit(
                channel=models.Channel('test channel'),
                operator=OperatorTestError()
            )
        ]
    )
    message = models.Message(models.Object(args=(3, )), ticket)

    channel, message = services.execute(message)

    assert channel == models.ChannelEnum.ERROR.value
    assert message.object.kwargs == {
        'error': 'Test error occur!',
        'operator': 'OperatorTestError',
        'args': models.Object(args=(3, )),
    }
    assert message.ticket == models.Ticket(
        ticket_id=models.TicketID('test ticket id'),
        units=[],
        num=0,
        is_last=True
    )


def test_execute_ok():
    operator_test_2 = OperatorTest2()

    ticket = models.Ticket(
        ticket_id=models.TicketID('test ticket id'),
        units=[
            models.Unit(
                channel=models.Channel('test channel 1'),
                operator=OperatorTest()
            ),
            models.Unit(
                channel=models.Channel('test channel 2'),
                operator=operator_test_2
            )
        ]
    )
    message = models.Message(
        models.Object(args=(3, )),
        ticket=ticket
    )

    channel, message = services.execute(message)

    assert channel == 'OperatorTest2'
    assert message.object == (9, )
    assert message.ticket == models.Ticket(
        ticket_id=models.TicketID('test ticket id'),
        units=[
            models.Unit(
                channel=models.Channel('test channel 2'),
                operator=operator_test_2,
            )
        ],
        num=0,
        is_last=True
    )
